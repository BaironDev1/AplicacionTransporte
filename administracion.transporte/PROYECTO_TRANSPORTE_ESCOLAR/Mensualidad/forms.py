from django import forms
from .models import Mensualidad
import datetime

class MensualidadForm(forms.ModelForm):
    # Defino el rango de años para el campo año_mensualidad
    current_year = datetime.date.today().year
    YEAR_CHOICES = [(year, year) for year in range(2023, current_year + 2)]  # Permite desde 2023 hasta 10 años en el futuro

    # Para monto solo dos opciones fijas
    MONTO_CHOICES = [
        (20000, '20.000 CLP'),
        (35000, '35.000 CLP'),
    ]

    año_mensualidad = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        label="Año de Mensualidad",
    )

    monto_mensualidad = forms.ChoiceField(
        choices=MONTO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        label="Monto Mensualidad",
    )

    class Meta:
        model = Mensualidad
        fields = ['pasajero', 'personal', 'año_mensualidad', 'mes_mensualidad', 'monto_mensualidad', 'pagado']

    def clean_año_mensualidad(self):
        año = int(self.cleaned_data['año_mensualidad'])
        if año < 2023:
            raise forms.ValidationError("El año debe ser entre 2023 o 2026.")
        return año

    def clean_monto_mensualidad(self):
        monto = int(self.cleaned_data['monto_mensualidad'])
        if monto not in [20000, 35000]:
            raise forms.ValidationError("El monto debe ser 20.000 CLP o 35.000 CLP.")
        return monto

