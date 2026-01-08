from django.shortcuts import render

# Create your views here.


def dashboard(request):
	"""Minimal reports dashboard view used by the main nav link."""
	return render(request, 'reports/dashboard.html')
