from django import forms
from .models import Sugerencia

class FormularioSugerencias (forms.ModelForm):
    class Meta:
        model = Sugerencia
        fields = ['nombre', 'email', 'sugerencia']

class FormularioSugerenciasUpdate (forms.ModelForm):
    class Meta:
        model = Sugerencia
        fields = ['sugerencia']