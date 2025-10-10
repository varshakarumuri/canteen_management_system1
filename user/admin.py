# user/admin.py
from django.contrib import admin
from .models import Users, Menu, Cart

admin.site.register(Users)
admin.site.register(Menu)
admin.site.register(Cart)