from django.urls import path
from .views import add_to_cart, cart_view, checkout

urlpatterns = [
    path('add/', add_to_cart, name="add_to_cart"),
    path('cart/', cart_view, name="cart"),
    path('checkout/', checkout, name="checkout"),
]