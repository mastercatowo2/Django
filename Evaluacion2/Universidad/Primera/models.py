
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    nro_celular = models.CharField(max_length=9)
    direccion = models.TextField()
    ramos_a_cursar = models.PositiveIntegerField()
    
    
class Docente(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    nro_celular = models.CharField(max_length=9)
    direccion = models.TextField()
    ramos_a_impartir = models.PositiveIntegerField()
    
    
class Ramo(models.Model):
    nombre = models.CharField(max_length=60)
    cantidad_notas = models.CharField(max_length=9)
    estado = models.BooleanField() 
    fecha_inicio = models.TextField()
    fecha_termino = models.TextField(max_length=9)
    numero_horas = models.PositiveIntegerField()
   
      