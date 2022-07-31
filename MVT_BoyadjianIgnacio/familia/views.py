from django.shortcuts import render
from django.http import HttpResponse
from familia.models import Familiares

# Create your views here.

def lista_familia(request):

    familiares = Familiares.objects.all()

    lista_familiares = []

    for familiar in familiares:
        lista_familiares.append[familiar.nombre]

    return HttpResponse(lista_familiares)
