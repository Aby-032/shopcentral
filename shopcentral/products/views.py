from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.

@login_required
#Products view
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
#Product Detail
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product})