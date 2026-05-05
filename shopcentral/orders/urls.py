from django.urls import path
from .views import add_to_cart, cart_view, checkout, my_orders, order_detail

urlpatterns = [
    path('add/', add_to_cart, name="add_to_cart"),
    path('cart/', cart_view, name="cart"),
    path('checkout/', checkout, name="checkout"),

    path('myorders/', my_orders, name="my_orders"),
    path('myorders/<int:id>', order_detail, name="order_detail"),
]