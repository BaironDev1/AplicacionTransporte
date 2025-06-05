from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Vistas para Personal
def lista_personal(request):
    personal = Personal.objects.all()
    return render(request, 'personal/lista_personal.html', {'personal': personal})

def crear_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personal')
    else:
        form = PersonalForm()
    return render(request, 'personal/crear_personal.html', {'form': form})

def editar_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('lista_personal')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'personal/editar_personal.html', {'form': form})

def eliminar_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        personal.delete()
        return redirect('lista_personal')
    return render(request, 'personal/eliminar_personal.html', {'personal': personal})

