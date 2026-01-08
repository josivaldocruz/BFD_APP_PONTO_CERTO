from django.shortcuts import render
from .models import Product


def list(request):
	"""Listagem simples de produtos usada pelo menu."""
	products = Product.objects.filter(is_active=True) if hasattr(Product, 'objects') else []
	return render(request, 'products/list.html', {'products': products})
