from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


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


def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')


def cerrar_sesion(request):
    pass
