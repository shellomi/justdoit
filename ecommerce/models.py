from django.db import models


class Product(models.Model):
    """docstring for Product"""
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
