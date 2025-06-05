from django import forms
from .models import Conductor, Vehiculo, Escuela, Usuario, RutaDiaria

# Conductor Form:
class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['rut_conductor', 'nombre_conductor', 'apellido_conductor', 'telefono_conductor', 'genero_conductor']
# Vehiculo Form:
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa_vehiculo', 'conductor', 'marca_vehiculo', 'modelo_vehiculo', 'año_vehiculo', 'capacidad_vehiculo']

# Escuela Form:
class EscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela
        fields = ['nombre_escuela', 'ubicacion_escuela']

# Usuario Form:
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut_usuario', 'escuela', 'nombre_usuario', 'apellido_usuario', 'representante_usuario', 'direccion_usuario']

# Viaje Form:
class RutaDiariaForm(forms.ModelForm):
    class Meta:
        model = RutaDiaria
        fields = ['usuario', 'vehiculo', 'fecha_viaje', 'hora_inicio', 'hora_fin']
    hora_inicio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    hora_fin = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
