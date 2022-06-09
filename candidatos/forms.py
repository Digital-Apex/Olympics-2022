from django import forms
from .models import *

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = CandidatoPresidente
        fields = ['nombre','apellidos','edad','cedula','profesion', 'partido']
        
class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuestas
        fields = '__all__'