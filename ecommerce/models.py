from django.db import models


class Directory(models.Model):
    """docstring for Directory"""
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Category(models.Model):
    """docstring for Category"""
    name = models.CharField(max_length=50)
    directory = models.ForeignKey(Directory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """docstring for Subcategory"""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """docstring for Product"""
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image_name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
