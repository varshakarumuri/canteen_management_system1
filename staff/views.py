from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Staff, ActiveOrders
from django.core.mail import send_mail
from django.conf import settings

# Utility function to handle sending emails
def send_custom_email(subject, message, recipient_list):
    """
    A utility function to send an email.
    """
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

# Your existing view for staff login
def staff_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            staff = Staff.objects.get(email=email)
            if check_password(password, staff.password):
                request.session['staff_id'] = staff.id
                return redirect('orders_page')
            else:
                return render(request, 'staff/login.html', {'error': 'Invalid credentials'})
        except Staff.DoesNotExist:
            return render(request, 'staff/login.html', {'error': 'Invalid credentials'})
    return render(request, 'staff/login.html')

# Your existing view for the orders page
def orders_page(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')

    active_orders = ActiveOrders.objects.all().order_by('order_id')
    grouped_orders = {}
    for order in active_orders:
        if order.order_id not in grouped_orders:
            grouped_orders[order.order_id] = {
                'items': [], 'user_name': order.user.name,
                'user_address': order.user.address, 'total': 0
            }
        grouped_orders[order.order_id]['items'].append(order)
        grouped_orders[order.order_id]['total'] += order.total_amount

    context = {
        'grouped_orders': grouped_orders,
        'total_orders_count': ActiveOrders.objects.values('order_id').distinct().count(),
    }
    return render(request, 'staff/orders.html', context)

# CORRECTED view for marking an order as ready
def order_ready(request, order_id):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')
    
    orders_to_remove = ActiveOrders.objects.filter(order_id=order_id)
    if orders_to_remove:
        # Get the user's email from the first item in the order
        user_email = orders_to_remove.first().user.email
        
        # Define the email subject and message
        subject = "Your E-Canteen Order is Ready!"
        message = f"Your order ({order_id}) is ready for pickup. Thank you for ordering!"
        
        # Call the utility function to send the email
        send_custom_email(subject, message, [user_email])
        
        # Delete the order from the active orders table
        orders_to_remove.delete()
        
    return redirect('orders_page')

# Your existing view for the staff profile
def staff_profile(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')
    staff = Staff.objects.get(id=staff_id)
    return render(request, 'staff/profile.html', {'staff': staff})

# Your existing view for staff logout
def staff_logout(request):
    if 'staff_id' in request.session:
        del request.session['staff_id']
    return redirect('home')