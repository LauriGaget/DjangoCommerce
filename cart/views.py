from django.shortcuts import render, HttpResponseRedirect
from cart.cart import Cart
from shop.models import Product
from users.models import UserCustom


def add_to_cart(request, product_id, user_id):
    product = Product.objects.get(id=product_id)
    user_id = user_id
    quantity = request.POST['quantity']
    cart = Cart(request, user_id)
    cart.add(product, product.price, quantity)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def remove_from_cart(request, product_id, user_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request, user_id)
    cart.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def get_cart(request, user_id):
    user_id = user_id
    return render(request, 'cart/cart.html', {'cart': Cart(request, user_id)})