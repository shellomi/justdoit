from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'ecommerce/index.html')


def stationery(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/stationery.html', {'products': products})
