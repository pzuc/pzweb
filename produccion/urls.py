from django.urls import path
from . import views

app_name = 'produccion'

urlpatterns = [
    path('', views.produccion, name = "Produccion"),   
    path('produccion_detalle/<int:proyecto_id>', views.produccion_detalle, name = "ProduccionDetalle"),  
]


