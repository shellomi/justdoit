from django.shortcuts import render


def home(request):
    return render(request, 'ecommerce/index.html')


def stationery(request):
    return render(request, 'ecommerce/stationery.html')
