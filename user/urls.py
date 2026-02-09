# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('register/', views.user_register, name='user_register'),
    path('menu/', views.menu_page, name='menu_page'),
    path('profile/', views.user_profile, name='user_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_page'),
    path('cart/increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('place-order/', views.place_order, name='place_order'),
]



