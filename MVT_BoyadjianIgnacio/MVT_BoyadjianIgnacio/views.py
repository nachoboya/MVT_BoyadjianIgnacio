from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def index(request):
    

    
    plantilla = loader.get_template("index.html")

    documento = plantilla.render()

    return HttpResponse(request)