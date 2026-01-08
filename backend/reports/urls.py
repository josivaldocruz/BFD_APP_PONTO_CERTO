from django.urls import path
from . import views

app_name = 'backend.reports'

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
]
