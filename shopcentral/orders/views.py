from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product

# Create your views here.

@login_required
# Add to Cart
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")

        product = get_object_or_404(Product, id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart = cart,
            product = product
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect("product_detail", id=product.id)