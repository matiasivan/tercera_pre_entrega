from django.db import models

class Curso(models.Model):
    Curso = models.CharField(max_length=40)
    nombre = models.IntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    curso_asignado = models.CharField(max_length=30)
