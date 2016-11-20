from django.db import models
from django.contrib import admin
from django.utils import timezone




class Marca(models.Model):
    marca1  =   models.CharField(max_length=30)
    def __str__(self):
        return self.marca1

class Modelo(models.Model):
    modelo1  =   models.CharField(max_length=30)
    def __str__(self):
        return self.modelo1

class Vehiculo(models.Model):
    fecha_ingreso = models.DateField(default=timezone.now)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='photo/')
    

class VehiculosInLine(admin.TabularInline):
    model = Vehiculo
    extra = 3

class MarcaAdmin(admin.ModelAdmin):
    inlines = (VehiculosInLine,)

class ModeloAdmin (admin.ModelAdmin):
    inlines = (VehiculosInLine,)