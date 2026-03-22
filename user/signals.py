# user/signals.py

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Menu, Cart
from staff.models import ActiveOrders, CompletedOrder
from django.core.mail import send_mail
from django.conf import settings


@receiver(pre_delete, sender=Menu)
def handle_menu_item_deletion(sender, instance, **kwargs):
    """
    Signal handler that runs when a Menu item is deleted.
    - Removes affected orders from ActiveOrders
    - Removes affected items from Cart
    - Sends notification email to affected users
    """
    
    item_to_delete = instance
    
    # Find all active orders containing this item
    affected_active_orders = ActiveOrders.objects.filter(item=item_to_delete)
    
    # Group affected users and their items
    affected_users_data = {}  # {user_id: {user_obj, email, [items]}}
    
    for order in affected_active_orders:
        user = order.user
        if user.id not in affected_users_data:
            affected_users_data[user.id] = {
                'user': user,
                'email': user.email,
                'items': []
            }
        affected_users_data[user.id]['items'].append(item_to_delete.item_name)
    
    # Delete all affected active orders
    affected_active_orders.delete()
    
    # Remove from cart if present
    cart_items = Cart.objects.filter(item=item_to_delete)
    cart_items.delete()
    
    # Send notification emails to affected users
    for user_id, user_data in affected_users_data.items():
        send_cancellation_email(user_data['email'], user_data['items'], user_data['user'].name)


def send_cancellation_email(email, items, user_name):
    """
    Sends email to user about cancelled items.
    """
    items_list = ', '.join(items)
    
    subject = "Order Item Cancellation - E-Canteen"
    message = f"""Dear Customer,

We regret to inform you that due to an unexpected issue with item quality, {items_list} from your recent order could not be fulfilled. The affected item(s) have been removed from your order, and the corresponding amount has been deducted. We sincerely apologize for the inconvenience and appreciate your understanding. For any queries, please feel free to contact our support team.

Warm regards,
Team E-Canteen"""
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        print(f"Cancellation email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send cancellation email to {email}. Error: {e}")
