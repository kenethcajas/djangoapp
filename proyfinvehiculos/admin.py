from django.contrib import admin
from proyfinvehiculos.models import Marca, Modelo, MarcaAdmin, ModeloAdmin, Vehiculo

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Vehiculo)