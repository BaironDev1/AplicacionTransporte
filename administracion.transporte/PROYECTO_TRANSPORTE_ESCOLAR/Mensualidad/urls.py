from django.urls import path
from . import views  # Asegúrate de que esta línea esté presente

urlpatterns = [
   # URLs para Mensualidad
    path('mensualidades/', views.lista_mensualidades, name='lista_mensualidades'),
    path('mensualidades/crear/', views.crear_mensualidad, name='crear_mensualidad'),
    path('mensualidades/editar/<int:pk>/', views.editar_mensualidad, name='editar_mensualidad'),
    path('mensualidades/eliminar/<int:pk>/', views.eliminar_mensualidad, name='eliminar_mensualidad'),
]

