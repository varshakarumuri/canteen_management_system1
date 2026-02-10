from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Users, Menu, Cart
from staff.models import ActiveOrders
import random
from django.core.mail import send_mail
from django.conf import settings 
def send_custom_email(subject, message, recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        print(f"Email sent successfully to {recipient_list}")
        return True
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        return False

otp_storage = {}

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('menu_page')
            else:
                return render(request, 'user/login.html', {'error': 'Invalid password'})
        except Users.DoesNotExist:
            return render(request, 'user/login.html', {'error': 'User not found'})
    
    # Check if there's a success message from password reset
    message = request.session.pop('password_reset_success', None)
    return render(request, 'user/login.html', {'message': message} if message else {})

def verify_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if Users.objects.filter(email=email).exists():
            return render(request, 'user/verify_email.html', {'error': 'Email already registered.'})

        otp = str(random.randint(1000, 9999))
        otp_storage[email] = otp
        
        subject = "Your OTP for E-Canteen"
        message = f"Your one-time password is: {otp}"
        send_custom_email(subject, message, [email])
        
        request.session['registration_email'] = email
        return render(request, 'user/verify_email.html', {'email': email, 'otp_sent': True})
        
    return render(request, 'user/verify_email.html')

def user_register(request):
    email = request.session.get('registration_email')
    if not email:
        return redirect('verify_email')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if otp_storage.get(email) == entered_otp:
            if 'name' in request.POST:
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                address = request.POST.get('address')
                password = request.POST.get('password')
                
                new_user = Users(
                    name=name,
                    email=email,
                    phone_number=phone,
                    address=address,
                    password=make_password(password)
                )
                new_user.save()
                
                del otp_storage[email]
                del request.session['registration_email']
                
                return redirect('user_login')
            else:
                return render(request, 'user/register.html', {'email': email})
        else:
            return render(request, 'user/verify_email.html', {'email': email, 'otp_sent': True, 'error': 'Invalid OTP'})
            
    return redirect('verify_email')

def menu_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    query = request.GET.get('q', '').strip()
    if query:
        menu_items = Menu.objects.filter(item_name__icontains=query)
    else:
        menu_items = Menu.objects.all()
    cart_items = Cart.objects.filter(user_id=user_id)
    user = Users.objects.get(id=user_id)

    total_amount = sum(item.item.price * item.quantity for item in cart_items)

    context = {
        'menu_items': menu_items,
        'cart_items': cart_items,
        'total_amount': total_amount,
        'user': user
    }
    return render(request, 'user/menu.html', context)

def add_to_cart(request, item_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    menu_item = Menu.objects.get(id=item_id)
    user = Users.objects.get(id=user_id)
    
    if menu_item.quantity > 0:
        cart_item, created = Cart.objects.get_or_create(user=user, item=menu_item)
        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()
        
        menu_item.quantity -= 1
        menu_item.save()
        
    return redirect('menu_page')

def place_order(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    user = Users.objects.get(id=user_id)
    cart_items = Cart.objects.filter(user=user)
    

    print('DEBUG: cart_items for receipt:', list(cart_items))
    if not cart_items:
        print('DEBUG: No cart items found for user', user)
        return redirect('menu_page')

    order_id = f"{user.id}-{random.randint(10000, 99999)}"

    cart_items_list = list(cart_items)
    for item in cart_items_list:
        ActiveOrders.objects.create(
            user=user,
            item=item.item,
            quantity=item.quantity,
            total_amount=item.item.price * item.quantity,
            order_id=order_id
        )

    total_bill = sum(item.item.price * item.quantity for item in cart_items_list)
    receipt_context = {
        'ordered_items': cart_items_list,
        'total_bill': total_bill,
        'message': 'Order placed successfully!'
    }

    cart_items.delete()

    return render(request, 'user/receipt.html', receipt_context)

def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def user_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    user = Users.objects.get(id=user_id)
    message = ''
    error = ''

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', '').strip()
        
        # Validate phone number: exactly 10 digits
        if not phone_number.isdigit() or len(phone_number) != 10:
            error = 'Phone number must be exactly 10 digits.'
        else:
            user.name = request.POST.get('name')
            user.phone_number = phone_number
            user.address = request.POST.get('address')
            user.save()
            message = 'Profile updated successfully!'

    return render(request, 'user/profile.html', {'user': user, 'message': message, 'error': error})


def change_password(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    user = Users.objects.get(id=user_id)
    error = ''
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        if check_password(old_password, user.password):
            user.password = make_password(new_password)
            user.save()
            return redirect('menu_page') 
        else:
            error = 'Incorrect old password.'

    return render(request, 'user/change_password.html', {'error': error})

def cart_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    cart_items = Cart.objects.filter(user_id=user_id)
    
    # Calculate subtotal for each cart item
    for item in cart_items:
        item.subtotal = item.item.price * item.quantity
    
    total_amount = sum(item.subtotal for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'user/cart.html', context)

def increase_quantity(request, cart_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    cart_item = Cart.objects.get(id=cart_id, user_id=user_id)
    menu_item = cart_item.item
    
    if menu_item.quantity > 0:
        cart_item.quantity += 1
        cart_item.save()
        menu_item.quantity -= 1
        menu_item.save()
    
    return redirect('cart_page')

def decrease_quantity(request, cart_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    cart_item = Cart.objects.get(id=cart_id, user_id=user_id)
    menu_item = cart_item.item
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        menu_item.quantity += 1
        menu_item.save()
    else:
        cart_item.delete()
        menu_item.quantity += 1
        menu_item.save()
    
    return redirect('cart_page')

def remove_from_cart(request, cart_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    
    cart_item = Cart.objects.get(id=cart_id, user_id=user_id)
    menu_item = cart_item.item
    
    menu_item.quantity += cart_item.quantity
    menu_item.save()
    cart_item.delete()
    
    return redirect('cart_page')

# Replace your old add_to_cart function with this one

def add_to_cart(request, item_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')

    try:
        menu_item = Menu.objects.get(id=item_id)
        user = Users.objects.get(id=user_id)
    except (Menu.DoesNotExist, Users.DoesNotExist):
        return redirect('menu_page')

    if menu_item.quantity > 0:
        cart_item, created = Cart.objects.get_or_create(
            user=user,
            item=menu_item,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        menu_item.quantity -= 1
        menu_item.save()
    return redirect('menu_page')

def forgot_password_verify(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if not Users.objects.filter(email=email).exists():
            return render(request, 'user/forgot_password.html', {'error': 'Email not found.'})

        otp = str(random.randint(1000, 9999))
        otp_storage[email] = otp
        
        subject = "Your OTP for Password Reset - E-Canteen"
        message = f"Your one-time password for password reset is: {otp}"
        send_custom_email(subject, message, [email])
        
        request.session['reset_email'] = email
        return render(request, 'user/forgot_password.html', {'email': email, 'otp_sent': True})
        
    return render(request, 'user/forgot_password.html')

def reset_password(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('forgot_password_verify')

    if request.method == 'POST':
        # Step 1: OTP Verification
        if 'otp' in request.POST:
            entered_otp = request.POST.get('otp')
            if otp_storage.get(email) == entered_otp:
                # OTP verified, show password reset form
                return render(request, 'user/reset_password.html', {'email': email, 'otp_verified': True})
            else:
                # Invalid OTP, go back to forgot password
                return render(request, 'user/forgot_password.html', {'email': email, 'otp_sent': True, 'error': 'Invalid OTP'})
        
        # Step 2: Password Update
        elif 'new_password' in request.POST:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            
            if new_password == confirm_password:
                # Update password in database
                user = Users.objects.get(email=email)
                user.password = make_password(new_password)
                user.save()
                
                # Clean up OTP storage
                if email in otp_storage:
                    del otp_storage[email]
                
                # Store success message in session
                request.session['password_reset_success'] = 'Password reset successfully! Please login with your new password.'
                
                # Clean up reset_email from session
                if 'reset_email' in request.session:
                    del request.session['reset_email']
                
                # Redirect to login
                return redirect('user_login')
            else:
                # Passwords don't match
                return render(request, 'user/reset_password.html', {'email': email, 'otp_verified': True, 'error': 'Passwords do not match.'})
            
    return redirect('forgot_password_verify')