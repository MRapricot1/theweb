from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

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


    def __str__(self):
        return self.name


    @property
    def is_products_hot(self):
        return self.products_views > 20

    def increment_views(self):
        Product.objects.filter(pk=self.pk).update(products_views=F('products_views') + 1)
        self.refresh_from_db(fields=['products_views'])
