from django.shortcuts import render

from django.views.generic import *

from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import *


# Create your views here.

class CreateCandidato(CreateView):
    template_name = 'candidatos/create.html'
    form_class = CandidatoForm
    success_url = reverse_lazy('candidatos:list')
    
class ListCandidato(ListView):
    template_name = 'candidatos/list.html'
    model = CandidatoPresidente
    context_object_name = 'candidatos'
    
class UpdateCandidato(UpdateView):
    template_name = 'candidatos/update.html'
    model = CandidatoPresidente
    form_class = CandidatoForm
    success_url = reverse_lazy('candidatos:list')

class DeleteCandidato(DeleteView):
    template_name = 'candidatos/delete.html'
    model = CandidatoPresidente
    success_url = reverse_lazy('candidatos:list')
    
class CreatePropuesta(CreateView):
    template_name = 'candidatos/create_propuesta.html'
    model = Propuestas
    form_class = PropuestaForm
    success_url = reverse_lazy('candidatos:propuesta_list')

class UpdatePropuesta(UpdateView):
    template_name = 'candidatos/update_propuesta.html'
    model = Propuestas
    form_class = PropuestaForm
    success_url = reverse_lazy('candidatos:propuesta_list')

class ListPropuesta(ListView):
    template_name = 'candidatos/list_propuesta.html'
    model = Propuestas

class DeletePropuesta(DeleteView):
    template_name = 'candidatos/delete_propuesta.html'
    model = Propuestas
    success_url = reverse_lazy('candidatos:propuesta_list')
    
def aumentarVoto(request, pk):
    candidato = CandidatoPresidente.objects.get(pk=pk)
    candidato.votos += 1
    candidato.save()
    return redirect('candidatos:list')

    

class ViewFrame(TemplateView):
    template_name = 'frame.html'


class ViewFrameTwo(TemplateView):
    template_name = 'frame_two.html'