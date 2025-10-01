from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid
from django.db import models

CATEGORY_CHOICES = [
    ('update', 'Update'),
    ('jersey', 'Jersey'),
    ('socks', 'Socks'),
    ('ball', 'Ball'),
    
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    products_views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)

class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()

    
    def __str__(self):
        return self.name
    
    @property
    def is_products_hot(self):
         return self.products_views > 20
        
    def increment_views(self):
        self.thumbnail
        self.save()
