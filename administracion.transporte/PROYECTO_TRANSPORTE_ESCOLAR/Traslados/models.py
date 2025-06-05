from django.db import models

class Conductor(models.Model):
    rut_conductor = models.CharField(max_length=12, unique=True)
    nombre_conductor = models.CharField(max_length=50)
    apellido_conductor = models.CharField(max_length=50)
    telefono_conductor = models.CharField(max_length=15)
    genero_conductor = models.CharField(max_length=10, choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')])

    def __str__(self):
        return f"{self.nombre_conductor} {self.apellido_conductor} - {self.rut_conductor}"

class Vehiculo(models.Model):
    placa_vehiculo = models.CharField(max_length=10, unique=True)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name='vehiculos')
    marca_vehiculo = models.CharField(max_length=50)
    modelo_vehiculo = models.CharField(max_length=50)
    año_vehiculo = models.IntegerField()
    capacidad_vehiculo = models.IntegerField()

    def __str__(self):
        return f"{self.marca_vehiculo} {self.modelo_vehiculo} - {self.placa_vehiculo}"

class Escuela(models.Model):
    codigo_escuela = models.AutoField(primary_key=True)
    nombre_escuela = models.CharField(max_length=100)
    ubicacion_escuela = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_escuela

class Usuario(models.Model):
    rut_usuario = models.CharField(max_length=12, unique=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='usuarios')
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    representante_usuario = models.CharField(max_length=50)
    direccion_usuario = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre_usuario} {self.apellido_usuario} - {self.rut_usuario}"

class RutaDiaria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='viajes')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='viajes')
    fecha_viaje = models.CharField(max_length=10, choices=[
        ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'), ('Viernes', 'Viernes')
    ])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Viaje {self.id} - Vehículo {self.placa_vehiculo} - Usuario {self.rut_usuario}"
    
