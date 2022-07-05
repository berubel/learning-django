from django.shortcuts import HttpResponse, render, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def evento_local(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Invalid user or password.')
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) # filter events by the user
    data = {'eventos': evento} # dictionary
    return render(request, 'schedule.html', data)