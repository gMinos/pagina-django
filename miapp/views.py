from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Preferencia


def principal(request):
    return render(request, 'principal.html')


def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('principal')
            except IntegrityError:
                return render(request, "registrarse.html", {
                    'form': UserCreationForm(),
                    'error': 'El usuario ya existe',
                })
        return render(request, 'registrarse.html', {
            'form': UserCreationForm(),
            'error': 'Las contraseñas no coinciden',
        })


def iniciar_session(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contrasena incorrectos'
            })
        else:
            login(request, user)
            return redirect('principal')


def cerrar_session(request):
    logout(request)
    return redirect('principal')


def contacto(request):
    return render(request, 'contacto.html')


def informacion_plato(request):
    return render(request, 'detalles_plato.html')


def comidas_preferidas(request):
    preferidas = Preferencia.objects.filter(
        usuario=request.user, preferido=True)
    return render(request, 'preferencias.html', {
        'preferencias': preferidas,
    })
