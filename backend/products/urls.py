from django.urls import path
from . import views

app_name = 'backend.products'

urlpatterns = [
	path('', views.list, name='list'),
]
