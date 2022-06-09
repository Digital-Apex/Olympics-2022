from django.urls import path, include
from .views import *

urlpatterns = [
    path('inicio/', view=ViewFrame.as_view(), name='inicio'),
]
