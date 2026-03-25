# user/models.py

from django.db import models
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='menu_photos/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name
    
    def delete(self, *args, **kwargs):
        # Delete the photo file from the filesystem before deleting the model
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super().delete(*args, **kwargs)

class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('user', 'item')