from django.shortcuts import redirect, render
from .forms import Contacto
from django.core.mail import send_mail

# Create your views here.

def contacto (request):

    if request.method == "POST":
        form = Contacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            sender = form.cleaned_data['email']
            recipients = ['paulazuc@gmail.com']
            subject = 'Mensaje desde la web'
            message = nombre + ' te ha enviado un mensaje. Su correo es: ' + sender + ' y su mensaje: ' + mensaje
            
            try:
                send_mail(subject, message, sender, recipients)
                return redirect('/contacto/?sent')
            except:
                return redirect('/contacto/?error')
            
    else:
        form = Contacto()

    return render(request, "contacto/contacto.html", {'form' : form})