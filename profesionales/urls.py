from django.urls import path
from . import views

urlpatterns = [
    path("cerrajero/crear/",views.crear_cerrajero, name= "crear_cerrajero"),
    path("electricista/crear/",views.crear_electricista, name= "crear_electricista"),
    path("plomero/crear/",views.crear_plomero, name= "crear_plomero"),
    path("cerrajeros/",views.lista_cerrajeros, name= "lista_cerrajeros")
]