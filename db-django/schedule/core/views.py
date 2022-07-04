from django.shortcuts import HttpResponse
from .models import Evento

# Create your views here.

def evento_local(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)