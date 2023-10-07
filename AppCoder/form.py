from django import forms

class ComentarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    comentario = forms.CharField(widget=forms.Textarea)

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Nombre del Curso')
    
