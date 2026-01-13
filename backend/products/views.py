from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def list(request):
	"""Listagem simples de produtos usada pelo menu."""
	products = Product.objects.filter(is_active=True) if hasattr(Product, 'objects') else []
	return render(request, 'products/list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos') # Ou 'home'
    else:
        form = ProductForm()
    return render(request, 'templates/products/product_form.html', {'form': form})