from django.db import models

class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} (Cerrajero)'

class Electricista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    matriculado = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} (Electricista)'


class Plomero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} (Plomero)'