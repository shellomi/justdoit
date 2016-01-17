from django.shortcuts import render
from . import models


def home(request):
    return render(request, 'ecommerce/index.html')


def stationery(request):
    directories = models.Directory.objects.all()
    categories = models.Category.objects.all()
    subcategories = models.Subcategory.objects.all()
    products = models.Product.objects.all()
    dirs = []
    for directory in directories:
        dirt = Dir(directory.pk, directory.name)
        for category in categories:
            if category.directory_id != directory.pk:
                continue
            cat = Cat(category.name)
            for subcategory in subcategories:
                if category.pk != subcategory.category_id:
                    continue
                sub = Sub(subcategory.name)
                cat.subcategories.append(sub)
            dirt.categories.append(cat)
        dirs.append(dirt)
    return render(request, 'ecommerce/stationery.html',
                  {'directories': dirs,
                   'products': products})


class Dir:
    """docstring for Dir"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.categories = []

    def __str__(self):
        return self.name


class Cat:
    """docstring for Cat"""
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def __str__(self):
        return self.name


class Sub:
    """docstring for Sub"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
