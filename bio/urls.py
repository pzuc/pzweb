from django.urls import path
from . import views

app_name = 'bio'

urlpatterns = [
    path('', views.bio, name = "Bio"),   
]


