from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import Medico
# from forms import UserLogin, UserRegister



def index(request):
    dados = Medico.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'index.html', {'dados':dados})


def mostrar(request, idbusca):
    dados = get_object_or_404(Medico, id=idbusca)
    return render(request, 'detMedico.html', {'dados':dados})


def buscar(request):
    x = request.GET['buscar']
    if x is None or not x:
        messages.add_message(request, messages.INFO, 'Digite um valor válido')
        return render(request, 'index.html')

    dados = Medico.objects.order_by('nome').filter(
        Q(nome__icontains=x) | Q(especialidade__icontains=x)
    )
    return render(request, 'index.html', {'dados':dados})


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')
