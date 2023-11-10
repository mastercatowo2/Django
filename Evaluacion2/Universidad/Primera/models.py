
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    nro_celular = models.CharField(max_length=9)
    direccion = models.TextField()
    ramos_a_cursar = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre