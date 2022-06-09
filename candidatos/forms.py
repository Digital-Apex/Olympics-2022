from django import forms
from .models import *

class CandidatoForm(forms.Form):
    class Meta():
        model = CandidatoPresidente
        fields = '__all__'
        
class PropuestaForm(forms.Form):
    class Meta():
        model = Propuestas
        fields = '__all__'