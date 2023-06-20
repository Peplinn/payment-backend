import requests
from django.shortcuts import render, redirect
from .models import Order, Product
# Create your views here.

def create_order(request):
    if request.method == 'POST':
        order = Order.objects.create()
        product_ids = request.POST.getlist('products')

        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            order.products.add(product)

        return redirect('checkout', order_id=order.id)
    
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'create_order.html', context) # Takes users back to create orders

def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'order': order}
    return render(request, 'checkout.html', context)

