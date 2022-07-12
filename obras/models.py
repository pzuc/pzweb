from tkinter import CASCADE
from django.db import models
from pymysql import NULL

# Create your models here.

class CategoriaObra(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "Categoria Obra"
        verbose_name_plural = "Categorias Obra"  

    def __str__(self):
        return self.nombre


class Obra (models.Model):
    titulo = models.CharField(max_length=50)
    disciplina = models.ForeignKey(CategoriaObra, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='obras', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='obras', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='obras', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='obras', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='obras', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    descripcion = models.TextField(default='')
    bajada = models.CharField(max_length=100, default='')
    lugar = models.CharField(max_length=100, default='Ushuaia')
    anio = models.PositiveIntegerField(default=2014)

    class Meta():
        #orden por defecto a menos que se sobreescriba otro orden
        ordering = ['-anio']

    def __str__(self):
        return self.titulo