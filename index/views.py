from django.shortcuts import render

def index(request):
    return render(request, "index/index.html", {})

def plantilla(request):
    datos = {
        "lista": ["Primero", "Segundo", "Tercero"],
        "nombre": "Juancho",
        "apellido": "Perez"
    }
    return render(request, "index/plantilla.html", datos)