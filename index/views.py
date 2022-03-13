from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("<H2>Bienvenidos!</H2>")

def plantilla(request):
    template = loader.get_template("plantilla.html")
    datos = {
        "lista": ["Primero", "Segundo", "Tercero"],
        "nombre": "Juancho",
        "apellido": "Perez"
    }
    plantilla_ok = template.render(datos)
    return HttpResponse(plantilla_ok)