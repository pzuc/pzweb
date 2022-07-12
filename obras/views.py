from tkinter import CASCADE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from obras import models
from .models import Obra, CategoriaObra
from .forms import FormularioCategoria
from django.forms import ModelForm
from django.db import models

# Create your views here.

# Create the form class. 
class ObraForm(ModelForm):   
    titulo = models.CharField(max_length=50)
    disciplina = models.ForeignKey(CategoriaObra, on_delete=models.CASCADE)
    #imagen = models.ImageField(upload_to='obras', null=True, blank=True)

    class Meta:
        model = Obra
        fields = ['titulo', 'disciplina', 'imagen']
          

def obras (request):
    if request.method == "POST":
        form = FormularioCategoria(request.POST)
        if form.is_valid():
            cat=form.cleaned_data["categoria"]
            obras = Obra.objects.filter(disciplina_id=cat)
    else:
        form = FormularioCategoria()
        obras = Obra.objects.all()
    categorias = CategoriaObra.objects.all()
    return render (request, "obras/obras.html", {'obras':obras, 'categorias':categorias, 'form':form})

def obras_alta (request):
    if request.method == "POST":
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, "obras/obras_alta.html")
    else:
        form = ObraForm()
    return render (request, "obras/obras_alta.html", {'form':form})


def obra_detalle(request, obra_id):
    obra = Obra.objects.get(id=obra_id)
    return render (request, "obras/obra_detalle.html", {'obra':obra})

