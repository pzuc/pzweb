from turtle import width
from django import forms
from pkg_resources import require
from .models import CategoriaObra

categorias = CategoriaObra.objects.all()
OPCIONES = []
for c in categorias:
    OPCIONES.append(
        (c.id, c.nombre)
    )

class FormularioCategoria(forms.Form):
    categoria= forms.CharField(widget=forms.Select(choices=OPCIONES))