# staff/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.staff_login, name='staff_login'),
    path('logout/', views.staff_logout, name='staff_logout'),
    path('orders/', views.orders_page, name='orders_page'),
    path('profile/', views.staff_profile, name='staff_profile'),

    # THIS IS THE LINE TO CHANGE:
    path('order-ready/<str:order_id>/', views.order_ready, name='order_ready'),
]