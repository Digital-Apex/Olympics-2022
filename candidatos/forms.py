from django import forms
from .models import *

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = CandidatoPresidente
        fields = ['nombre','apellidos','edad','cedula','profesion', 'partido', 'url', 'propuesta_1', 'propuesta_2', 'propuesta_3']
        
class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuestas
        fields = '__all__'