from django.urls import path
from AppCoder import views

urlpatterns = [
    path('cursos/', views.cursos),
    path('estudiantes/', views.estudiantes),
    path('profesor', views.profesor)
    
    
]
