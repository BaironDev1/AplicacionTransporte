from django.db import models
from django.core.validators import MinValueValidator
from Traslados.models import Usuario
from Personal.models import Personal

class Mensualidad(models.Model):
    pasajero = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensualidades')
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, related_name='mensualidades')
    año_mensualidad = models.IntegerField(validators=[MinValueValidator(1)])  # Año no puede ser menor a 1
    mes_mensualidad = models.CharField(max_length=20)
    monto_mensualidad = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pasajero.nombre_usuario} - {self.mes_mensualidad} {self.año_mensualidad}"

