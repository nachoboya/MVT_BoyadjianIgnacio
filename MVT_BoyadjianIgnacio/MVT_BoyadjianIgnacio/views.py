from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def index(request, name):
    
    datos = {"fecha_actual":datetime.now(), "username": name}
    
    plantilla = loader.get_template("index.html")

    documento = plantilla.render(datos)

    return HttpResponse(request)