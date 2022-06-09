from django.urls import path, include
from .views import *

urlpatterns = [
    path('inicio/', view=ViewFrame.as_view(), name='inicio'),
    path('opciones/', view=ViewFrameTwo.as_view(), name='opciones'),
    
    path('crear/', view=CreateCandidato.as_view(), name='create'),
    path('listar/', view=ListCandidato.as_view(), name='list'),
    path('editar/<int:pk>/', view=UpdateCandidato.as_view(), name='update'),
    path('eliminar/<int:pk>/', view=DeleteCandidato.as_view(), name='delete'),
    
    path('crear_propuesta/', view=CreatePropuesta.as_view(), name='create_propuesta'),
    path('listar_propuesta/', view=ListPropuesta.as_view(), name='list_propuesta'),
    path('editar_propuesta/<int:pk>/', view=UpdatePropuesta.as_view(), name='update_propuesta'),
    path('eliminar_propuesta/<int:pk>/', view=DeletePropuesta.as_view(), name='delete_propuesta'),
    
    path('aumentar/<int:pk>/', view=aumentarVoto, name='votar'),
]
