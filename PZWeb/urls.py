"""PZWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from obras import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('inicio.urls')),  
    path('admin/', admin.site.urls),
    path('obras/', include('obras.urls')),
    path('bio/', include('bio.urls')),
    path('produccion/', include('produccion.urls')),
    path('contacto/', include('contacto.urls')),
    #path('obras/', views.obras, name = "Obras"),   ESTO SI FUNCIONA SIN EL INCLUDE
]

#Esta linea para que se muestren ok las imagenes.
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)