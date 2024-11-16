from django.shortcuts import render
from shop.models import Product


def catalog(request):
    return render(request, 'shop/catalog.html', {
        'products': Product.objects.all()
    } )
