from django.urls import path
from .views import products_view, product_detail

urlpatterns = [
    path('products/', products_view, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail')
]