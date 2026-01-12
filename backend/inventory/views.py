from django.shortcuts import render
from .models import StockMovement


def movements(request):
	"""Lista de movimentações de estoque para o menu."""
	qs = StockMovement.objects.select_related('product', 'user').order_by('-created_at')[:100]
	return render(request, 'inventory/movements.html', {'movements': qs})
