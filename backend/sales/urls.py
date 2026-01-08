from django.urls import path
from . import views

app_name = 'backend.sales'

urlpatterns = [
    path('pos/', views.pos, name='pos'),
    path('api/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('api/remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('api/checkout/', views.checkout, name='checkout'),
]