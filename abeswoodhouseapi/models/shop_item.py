from django.db import models

class ShopItem(models.Model):
    """Represents an item in the shop"""
    
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=55)