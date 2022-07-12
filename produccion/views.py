from django.shortcuts import render

from produccion.models import Produccion

# Create your views here.


def produccion(request):
    proyectos = Produccion.objects.all()

    return render(request, 'produccion/produccion.html', {'proyectos':proyectos})

def produccion_detalle(request, proyecto_id):
    proyecto = Produccion.objects.get(id=proyecto_id)
    return render(request, 'produccion/produccion_detalle.html', {'proyecto':proyecto})

