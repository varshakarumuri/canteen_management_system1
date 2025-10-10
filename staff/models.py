# staff/models.py

from django.db import models
from user.models import Users, Menu

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class ActiveOrders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    order_id = models.CharField(max_length=100, default='default_order_id')

    def __str__(self):
        return f"Order for {self.user.name} - {self.item.item_name}"