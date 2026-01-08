from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Sale, SaleItem, Payment
from products.models import Product
from cash.models import CashSession

@login_required
def pos(request):
    # Verificar se há uma sessão de caixa aberta para o usuário
    cash_session = CashSession.objects.filter(operator=request.user, status='open').last()
    context = {
        'cash_session': cash_session,
    }
    return render(request, 'sales/pos.html', context)

@login_required
@require_http_methods(["POST"])
def add_to_cart(request):
    # Lógica para adicionar item ao carrinho (venda pendente)
    pass

@login_required
@require_http_methods(["POST"])
def remove_from_cart(request):
    pass

@login_required
@require_http_methods(["POST"])
def checkout(request):
    pass