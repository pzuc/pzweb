from distutils.command.upload import upload
from django.db import models
from pymysql import NULL

# Create your models here.

class Produccion(models.Model):

    titulo = models.CharField(max_length=100)
    bajada = models.CharField(max_length=300)
    descripcion = models.TextField(default='')
    lugar = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='produccion', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='produccion', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='produccion', blank=True, null=True)
    imagen4 = models.ImageField(upload_to='produccion', blank=True, null=True)
    imagen5 = models.ImageField(upload_to='produccion', blank=True, null=True)
    anio = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        #orden por defecto a menos que se sobreescriba otro orden
        ordering = ['-anio']
        verbose_name = "Producción"
        verbose_name_plural = "Producciones"

    def __str__(self):
        return self.titulo

