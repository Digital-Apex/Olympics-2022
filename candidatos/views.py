from django.shortcuts import render

from django.views.generic import *

from django.urls import reverse_lazy
from .forms import *


# Create your views here.

class CreateCandidato(TemplateView):
    template_name = 'candidatos/create.html'
    form_class = CandidatoForm
    success_url = reverse_lazy('candidatos:list')
    
class ListCandidato(ListView):
    template_name = 'candidatos/list.html'
    model = CandidatoPresidente
    
class UpdateCandidato(UpdateView):
    model = CandidatoPresidente
    form_class = CandidatoForm
    success_url = reverse_lazy('candidatos:list')

class DeleteCandidato(DeleteView):
    model = CandidatoPresidente
    success_url = reverse_lazy('candidatos:list')
    
class CreatePropuesta(CreateView):
    model = Propuestas
    form_class = PropuestaForm
    success_url = reverse_lazy('candidatos:propuesta_list')

class UpdatePropuesta(UpdateView):
    model = Propuestas
    form_class = PropuestaForm
    success_url = reverse_lazy('candidatos:propuesta_list')

class ListPropuesta(ListView):
    model = Propuestas

class DeletePropuesta(DeleteView):
    model = Propuestas
    success_url = reverse_lazy('candidatos:propuesta_list')
    
    

    

class ViewFrame(TemplateView):
    template_name = 'frame.html'


class ViewFrameTwo(TemplateView):
    template_name = 'frame_two.html'