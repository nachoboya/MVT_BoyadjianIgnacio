from django.shortcuts import render

from django.http import HttpResponse

from familia.models import Familiares

# Create your views here.

def lista_familia(request):

    familiares = Familiares.objects.all()

    return render(request, "index.html", {"familia" : familiares})