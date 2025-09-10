from django.db import models

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
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
