from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Staff, ActiveOrders, CompletedOrder
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

def order_ready(request, order_id):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')
    orders_to_remove = ActiveOrders.objects.filter(order_id=order_id)
    if orders_to_remove:
        user_email = orders_to_remove.first().user.email
        subject = "Your E-Canteen Order is Ready!"
        message = f"Your order ({order_id}) is ready for pickup. Thank you for ordering!"
        send_custom_email(subject, message, [user_email])
        # Move each ActiveOrders entry into CompletedOrder before deleting
        for order in orders_to_remove:
            CompletedOrder.objects.create(
                user=order.user,
                item=order.item,
                quantity=order.quantity,
                total_amount=order.total_amount,
                order_id=order.order_id,
            )
        orders_to_remove.delete()
    return redirect('orders_page')

def staff_profile(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')
    staff = Staff.objects.get(id=staff_id)
    return render(request, 'staff/profile.html', {'staff': staff})


def completed_orders_view(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')
    
    # Get only today's completed orders
    today = timezone.now().date()
    completed = CompletedOrder.objects.filter(completed_at__date=today).order_by('-completed_at')
    
    # Group orders by order_id
    grouped_completed_orders = {}
    for order in completed:
        if order.order_id not in grouped_completed_orders:
            grouped_completed_orders[order.order_id] = {
                'items': [],
                'user_name': order.user.name,
                'user_address': order.user.address,
                'total': 0,
                'completed_at': order.completed_at
            }
        grouped_completed_orders[order.order_id]['items'].append(order)
        grouped_completed_orders[order.order_id]['total'] += order.total_amount
    
    # Calculate today's totals
    today_order_ids = completed.values('order_id').distinct().count()
    today_total_amount = sum(order.total_amount for order in completed)
    
    context = {
        'grouped_completed_orders': grouped_completed_orders,
        'today_orders_count': today_order_ids,
        'today_total_amount': today_total_amount,
    }
    return render(request, 'staff/completed_orders.html', context)

def staff_logout(request):
    if 'staff_id' in request.session:
        del request.session['staff_id']
    return redirect('home')