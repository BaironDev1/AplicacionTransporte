from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Asegúrate de que esto esté definido
    
]
