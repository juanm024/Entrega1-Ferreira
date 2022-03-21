from django.shortcuts import redirect, render

from.models import Cerrajero, Electricista, Plomero
from .forms import CerrajerosBusqueda, CerrajeroFormulario, ElectricistaFormulario, PlomeroFormulario

# Create your views here.

def crear_cerrajero(request):

    if request.method == "POST":
        form = CerrajeroFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            cerrajero = Cerrajero(nombre=data["nombre"], apellido=data["apellido"], desempleado=data["desempleado"])
            cerrajero.save()

    form = CerrajeroFormulario()
    return render(request, "profesionales/crear_cerrajero.html", {"form": form})


def crear_electricista(request):

    if request.method == "POST":
        form = ElectricistaFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            electricista = Electricista(nombre=data["nombre"], apellido=data["apellido"], matriculado=data["matriculado"])
            electricista.save()

    form = ElectricistaFormulario()
    return render(request, "profesionales/crear_electricista.html", {"form": form})


def crear_plomero(request):

    if request.method == "POST":
        form = PlomeroFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            plomero = Plomero(nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"])
            plomero.save()

    form = PlomeroFormulario()
    return render(request, "profesionales/crear_plomero.html", {"form": form})


def lista_cerrajeros(request):

    nombre_buscar = request.GET.get("nombre", None)
    apellido_buscar = request.GET.get("apellido", None)
    
    if nombre_buscar is not None:
        cerrajeros = Cerrajero.objects.filter(nombre__icontains=nombre_buscar)
    elif apellido_buscar is not None:
        cerrajeros = Cerrajero.objects.filter(apellido__icontains=apellido_buscar)
    else:
        cerrajeros = Cerrajero.objects.all()

    form = CerrajerosBusqueda()
    return render(request, "profesionales/lista_cerrajeros.html", {"form": form, "cerrajeros": cerrajeros})