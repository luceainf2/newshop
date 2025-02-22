from django.shortcuts import render
from shop.models import Product, Order



def shorten_description(description, max_length=100):
    if len(description) > max_length:
        return description[:max_length] + "..."
    return description

def catalog(request):
    return render(request, 'shop/catalog.html', {
        'products': Product.objects.all(),
        'desc': shorten_description
    } )


def orders(request):
    orders = Order.objects.all()
    return render(request, 'shop/orders.html', {'orders': orders})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'shop/products_detail.html', {'product': product})

def order_create(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        order=Order.objects.create(product=product, delivery_address=request.POST['delivery_addres'])
    return render(request,'shop/order_create.html', {'product': product})



