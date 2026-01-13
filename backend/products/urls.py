from django.urls import path
from . import views

app_name = 'backend.products'

urlpatterns = [
	path('', views.list, name='list'),
    path('add/', views.product_create, name='product_add'),
]
