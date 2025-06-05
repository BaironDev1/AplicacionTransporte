from django.urls import path
from . import views

urlpatterns = [
    # URLs para los Choferes
    path('conductores/', views.lista_conductores, name='lista_conductores'),
    path('conductores/crear/', views.crear_conductor, name='crear_conductor'),
    path('conductores/editar/<int:pk>/', views.editar_conductor, name='editar_conductor'),
    path('conductores/eliminar/<int:pk>/', views.eliminar_conductor, name='eliminar_conductor'),

    # URLs para Vehículos que usarán los Choferes
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),

    # URLs para Escuelas de los Usuarios
    path('escuelas/', views.lista_escuelas, name='lista_escuelas'),
    path('escuelas/crear/', views.crear_escuela, name='crear_escuela'),
    path('escuelas/editar/<int:pk>/', views.editar_escuela, name='editar_escuela'),
    path('escuelas/eliminar/<int:pk>/', views.eliminar_escuela, name='eliminar_escuela'),

    # URLs para Usuarios de las Escuelas
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    # URLs para Viajes:
    path('rutas/', views.lista_rutas, name='lista_rutas'),  
    path('rutas/crear/', views.crear_ruta, name='crear_ruta'),  
    path('rutas/editar/<int:pk>/', views.editar_ruta, name='editar_ruta'),  
    path('rutas/eliminar/<int:pk>/', views.eliminar_ruta, name='eliminar_ruta'),  
]
