from django.shortcuts import render, redirect, get_object_or_404
from .models import RutaDiaria, Escuela, Usuario, Conductor, Vehiculo
from .forms import RutaDiariaForm, EscuelaForm, UsuarioForm, ConductorForm, VehiculoForm
from django.db.models import Q


def lista_conductores(request):
    consulta = request.GET.get('busqueda')
    if consulta:
        conductores = Conductor.objects.filter(
            Q(identificacion_conductor__icontains=consulta) |
            Q(nombre_conductor__icontains=consulta) |
            Q(apellido_conductor__icontains=consulta) |
            Q(numero_conductor__icontains=consulta) |
            Q(genero_conductor__icontains=consulta)
        )
    else:
        conductores = Conductor.objects.all()
    return render(request, 'conductores/lista_conductores.html', {'conductores': conductores})

def crear_conductor(request):
    if request.method == 'POST':
        formulario = ConductorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_conductores')
    else:
        formulario = ConductorForm()
    return render(request, 'conductores/crear_conductor.html', {'formulario': formulario})

def editar_conductor(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        formulario = ConductorForm(request.POST, instance=conductor)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_conductores')
    else:
        formulario = ConductorForm(instance=conductor)
    return render(request, 'conductores/editar_conductor.html', {'formulario': formulario})

def eliminar_conductor(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        conductor.delete()
        return redirect('lista_conductores')
    return render(request, 'conductores/eliminar_conductor.html', {'conductor': conductor})


# Vista para Vehículos:
def lista_vehiculos(request):
    consulta = request.GET.get('busqueda')
    if consulta:
        vehiculos = Vehiculo.objects.filter(
            Q(placa_vehiculo__icontains=consulta) |
            Q(conductor__nombre_conductor__icontains=consulta) |
            Q(conductor__apellido_conductor__icontains=consulta) |
            Q(marca_vehiculo__icontains=consulta) |
            Q(modelo_vehiculo__icontains=consulta) |
            Q(anio_vehiculo__icontains=consulta) |
            Q(capacidad_vehiculo__icontains=consulta)
        )
    else:
        vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/lista_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_vehiculos')
    else:
        formulario = VehiculoForm()
    return render(request, 'vehiculos/crear_vehiculo.html', {'formulario': formulario})

def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_vehiculos')
    else:
        formulario = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/editar_vehiculo.html', {'formulario': formulario})

def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'vehiculos/eliminar_vehiculo.html', {'vehiculo': vehiculo})


# Vista para Escuelas:
def lista_escuelas(request):
    consulta = request.GET.get('busqueda')
    if consulta:
        escuelas = Escuela.objects.filter(
            Q(nombre_escuela__icontains=consulta) |
            Q(direccion_escuela__icontains=consulta)
        )
    else:
        escuelas = Escuela.objects.all()
    return render(request, 'escuelas/lista_escuelas.html', {'escuelas': escuelas})

def crear_escuela(request):
    if request.method == 'POST':
        formulario = EscuelaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_escuelas')
    else:
        formulario = EscuelaForm()
    return render(request, 'escuelas/crear_escuela.html', {'formulario': formulario})

def editar_escuela(request, pk):
    escuela = get_object_or_404(Escuela, pk=pk)
    if request.method == 'POST':
        formulario = EscuelaForm(request.POST, instance=escuela)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_escuelas')
    else:
        formulario = EscuelaForm(instance=escuela)
    return render(request, 'escuelas/editar_escuela.html', {'formulario': formulario})

def eliminar_escuela(request, pk):
    escuela = get_object_or_404(Escuela, pk=pk)
    if request.method == 'POST':
        escuela.delete()
        return redirect('lista_escuelas')
    return render(request, 'escuelas/eliminar_escuela.html', {'escuela': escuela})


# Vista para Usuarios
def lista_usuarios(request):
    consulta = request.GET.get('busqueda')
    if consulta:
        usuarios = Usuario.objects.filter(  # Cambia 'Estudiante' por 'Usuario'
            Q(identificacion_usuario__icontains=consulta) |
            Q(nombre_usuario__icontains=consulta) |
            Q(apellido_usuario__icontains=consulta) |
            Q(apoderado_usuario__icontains=consulta) |
            Q(direccion_usuario__icontains=consulta)
        )
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)  # Cambia 'EstudianteForm' por 'UsuarioForm'
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')  # Cambia la redirección a 'lista_usuarios'
    else:
        formulario = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'formulario': formulario})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)  # Cambia 'Estudiante' por 'Usuario'
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, instance=usuario)  # Cambia 'EstudianteForm' por 'UsuarioForm'
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')  # Cambia la redirección a 'lista_usuarios'
    else:
        formulario = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'formulario': formulario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)  # Cambia 'Estudiante' por 'Usuario'
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')  # Cambia la redirección a 'lista_usuarios'
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})  # Cambia 'estudiante' por 'usuario'


# Vista para Rutas Diarias:
def lista_rutas(request):
    consulta = request.GET.get('busqueda')
    if consulta:
        rutas = RutaDiaria.objects.filter(
            Q(dia_ruta__icontains=consulta) |
            Q(hora_inicio__icontains=consulta) |
            Q(hora_fin__icontains=consulta)
        )
    else:
        rutas = RutaDiaria.objects.all()
    return render(request, 'rutas/lista_rutas.html', {'rutas': rutas})

def crear_ruta(request):
    if request.method == 'POST':
        formulario = RutaDiariaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_rutas')
    else:
        formulario = RutaDiariaForm()
    return render(request, 'rutas/crear_ruta.html', {'formulario': formulario})

def editar_ruta(request, pk):
    ruta = get_object_or_404(RutaDiaria, pk=pk)
    if request.method == 'POST':
        formulario = RutaDiariaForm(request.POST, instance=ruta)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_rutas')
    else:
        formulario = RutaDiariaForm(instance=ruta)
    return render(request, 'rutas/editar_ruta.html', {'formulario': formulario})

def eliminar_ruta(request, pk):
    ruta = get_object_or_404(RutaDiaria, pk=pk)
    if request.method == 'POST':
        ruta.delete()
        return redirect('lista_rutas')
    return render(request, 'rutas/eliminar_ruta.html', {'ruta': ruta})
