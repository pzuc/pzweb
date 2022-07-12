from django.shortcuts import render
from obras.models import Obra


# Create your views here.

def inicio (request):
    obras = Obra.objects.all().order_by('-anio')[:3]
    return render (request, "inicio/index.html", {'obras':obras})   