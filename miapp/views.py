from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CrearFormularioPreferencia
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
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contrasena incorrectos'
            })
        else:
            login(request, user)
            return redirect('principal')


@login_required
def cerrar_session(request):
    logout(request)
    return redirect('principal')


def contacto(request):
    return render(request, 'contacto.html')


def informacion_plato(request):
    return render(request, 'detalles_plato.html')


@login_required
def comidas_preferidas(request):
    preferidas = Preferencia.objects.filter(
        usuario=request.user, preferido=True)
    return render(request, 'preferencias.html', {
        'preferencias': preferidas,
    })


@login_required
def editar_preferencia(request, id_preferencia):
    preferencia = get_object_or_404(Preferencia, pk=id_preferencia, usuario=request.user)
    try:
        if request.method == 'GET':
            form = CrearFormularioPreferencia(instance=preferencia)
            return render(request, 'editar_preferencia.html', {
                'preferencia': preferencia,
                'form': form,
            })
        else:
            form = CrearFormularioPreferencia(request.POST, instance=preferencia)
            form.save()
            return redirect('preferencias')
    except ValueError:
        return render(request, 'editar_preferencia.html', {
            'preferencia': preferencia,
            'form': form,
            'error': 'Error al actualizar la preferencia',
        })


@login_required()
def eliminar_preferencia(request, id_preferencia):
    preferencia = get_object_or_404(Preferencia, pk=id_preferencia, usuario=request.user)
    if request.method == 'POST':
        preferencia.delete()
        return redirect('preferencias')


@login_required
def agregar_preferencia(request):
    if request.method == 'POST':
        try:
            form = CrearFormularioPreferencia(request.POST).save(commit=False)
            form.usuario = request.user
            form.save()
            return redirect('preferencias')
        except ValueError:
            return render(request, 'agregar_preferencia.html', {
                'form': CrearFormularioPreferencia(),
                'error': 'Error al agregar preferencia',
            })
    else:
        return render(request, 'agregar_preferencia.html', {
            'form': CrearFormularioPreferencia()
        })
