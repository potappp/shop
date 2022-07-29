from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=127)
    vendor = models.CharField(max_length=31)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    media = models.FileField(upload_to='video/%Y/%m/%d/', blank=True)

    purpose_price = models.IntegerField()
    sale_price = models.IntegerField(blank=True)
    gain = models.IntegerField(blank=True)
    duration_of_sale = models.TimeField(blank=True)

    buyer = models.CharField(max_length=31)
    seller = models.CharField(max_length=31)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bought_at = models.DateTimeField(blank=True)
    sale_at = models.DateTimeField(blank=True)

    is_published = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
