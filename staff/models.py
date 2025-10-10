# staff/models.py

from django.db import models
from user.models import Users, Menu # Import models from the user app

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) # Store hashed passwords

    def __str__(self):
        return self.name

class ActiveOrders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    # You might want to add an order_id to group items from the same order
    order_id = models.CharField(max_length=100, default='default_order_id') 

    def __str__(self):
        return f"Order for {self.user.name} - {self.item.item_name}"