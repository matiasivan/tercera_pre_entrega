from django.urls import path
from . import views

      
urlpatterns = [
    
    path('cursos/', views.cursos, name="Cursos"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesor/', views.profesor, name="Profesor"),
    path('agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('buscar_cursos/', views.buscar_cursos, name='buscar_cursos')
    
     ]
