from django.shortcuts import render
from .form import ComentarioForm , BuscarCursoForm
from .models import Curso

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesor(request):
    return render(request, "AppCoder/profesor.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            
            return render(request, 'tu_app/comentario_exitoso.html')  
    else:
        form = ComentarioForm()

    return render(request, 'tu_app/agregar_comentario.html', {'form': form})


def buscar_cursos(request):
    cursos = None
    if request.method == 'POST':
        form = BuscarCursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            cursos = Curso.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarCursoForm()
    
    return render(request, 'tu_app/buscar_cursos.html', {'form': form, 'cursos': cursos})


