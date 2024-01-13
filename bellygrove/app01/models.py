# models.py
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255)
    roomNumber = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=10)

class Order(models.Model):
    cart_data = models.JSONField()
    