from django.shortcuts import render
from .models import CashSession


def sessions(request):
	"""Lista de sessões de caixa para o menu."""
	qs = CashSession.objects.select_related('operator').order_by('-opened_at')[:50]
	return render(request, 'cash/sessions.html', {'sessions': qs})
