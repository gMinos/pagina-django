from django import forms
from .models import Preferencia


class CrearFormularioPreferencia(forms.ModelForm):
    class Meta:
        model = Preferencia
        fields = ('nombre_plato_preferido', 'motivo_preferencia')
