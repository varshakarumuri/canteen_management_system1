from django.contrib import admin
from .models import Staff, ActiveOrders
from django.contrib.auth.hashers import make_password


class StaffAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    def save_model(self, request, obj, form, change):
        # This line hashes the password
        if 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(Staff, StaffAdmin)
admin.site.register(ActiveOrders)