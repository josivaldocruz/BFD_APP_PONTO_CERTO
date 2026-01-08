from django.urls import path
from . import views

app_name = 'backend.cash'

urlpatterns = []
 
urlpatterns = [
	path('sessions/', views.sessions, name='sessions'),
]
