from django.urls import path
from . import views

urlpatterns = [
    # URLs para Personal
    path('personal/', views.lista_personal, name='lista_personal'),
    path('personal/crear/', views.crear_personal, name='crear_personal'),
    path('personal/editar/<int:pk>/', views.editar_personal, name='editar_personal'),
    path('personal/eliminar/<int:pk>/', views.eliminar_personal, name='eliminar_personal'),
]