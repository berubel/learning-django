from django.shortcuts import HttpResponse, render, redirect
from .models import Evento

# Create your views here.

def evento_local(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all() # get all objects
    data = {'eventos': evento} # dictionary
    return render(request, 'schedule.html', data)