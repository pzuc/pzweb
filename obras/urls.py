from django.urls import path
from . import views

app_name = 'obras'

urlpatterns = [
    path('', views.obras, name = "Obras"),   
    path('obras_alta/', views.obras_alta, name = "ObrasAlta"),   
    path('obras_detalle/<int:obra_id>', views.obra_detalle, name = "ObraDetalle"),  
]


