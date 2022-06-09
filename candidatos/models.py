from django.db import models

# Create your models here.



class Propuestas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=800)

class CandidatoPresidente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=10)
    votos = models.IntegerField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} ~ {}'.format(self.nombre, self.apellidos, self.votos)
    
    