from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Vistas Menusalidades
def lista_mensualidades(request):
    mensualidades = Mensualidad.objects.all()
    return render(request, 'mensualidades/lista_mensualidades.html', {'mensualidades': mensualidades})


def crear_mensualidad(request):
    if request.method == 'POST':
        form = MensualidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mensualidades')
    else:
        form = MensualidadForm()
    return render(request, 'mensualidades/crear_mensualidad.html', {'form': form})

def editar_mensualidad(request, pk):
    mensualidad = get_object_or_404(Mensualidad, pk=pk)
    if request.method == 'POST':
        form = MensualidadForm(request.POST, instance=mensualidad)
        if form.is_valid():
            form.save()
            return redirect('lista_mensualidades')
    else:
        form = MensualidadForm(instance=mensualidad)
    return render(request, 'mensualidades/editar_mensualidad.html', {'form': form})


def eliminar_mensualidad(request, pk):
    mensualidad = get_object_or_404(Mensualidad, pk=pk)
    if request.method == 'POST':
        mensualidad.delete()
        return redirect('lista_mensualidades')
    return render(request, 'mensualidades/eliminar_mensualidad.html', {'mensualidad': mensualidad})

