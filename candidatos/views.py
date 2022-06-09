from django.shortcuts import render

from django.views.generic import *


# Create your views here.

class CreateCandidato(View):
    def get(self, request):
        return render(request, 'candidatos/create_candidato.html')
    
    
class ViewFrame(TemplateView):
    template_name = 'frame.html'
