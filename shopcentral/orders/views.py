from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem, Order, OrderItem
from products.models import Product

# Create your views here.

@login_required # Add to Cart View
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

    return redirect("products")

@login_required # Cart View
def cart_view(request):
    cart = Cart.objects.get(user=request.user)

    cart_items = cart.items.all()

    total = sum(item.subtotal for item in cart_items)

    return render(request, 'orders/cart.html', {
        "cart": cart,
        "cart_items": cart_items,
        "total": total
    })

@login_required # Checkout
def checkout(request):
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()

        if not cart_items.exists():
            return redirect('cart')

        total = sum(item.subtotal for item in cart_items)
        order = Order.objects.create(
            user = request.user,
            total_price = total,
            status = "PENDING"
        )

        for item in cart_items:
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price
            )

        cart_items.delete()

        messages.success(request, "Order placed successfully!")
    
    return redirect('my_orders')

@login_required # Orders / Order Summary
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required # Order Detail
def order_detail(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    order_items = order.items.all()

    return render(request, 'orders/order_detail.html', {
        "order": order,
        "order_items": order_items
    })