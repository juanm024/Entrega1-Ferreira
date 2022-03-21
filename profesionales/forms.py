from django import forms

class CerrajeroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    desempleado = forms.BooleanField(required=False)

class ElectricistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    matriculado = forms.BooleanField(required=False)

class PlomeroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()

class CerrajerosBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)