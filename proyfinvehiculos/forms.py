from django import forms
from .models import Vehiculo, Marca, Modelo



class VehiculoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Vehiculo
        fields = ( 'marca', 'modelo','imagen')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


def __init__ (self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["marca"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["marca"].help_text = "Seleccione la marca del vehiculo"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["marca"].queryset = Marca.objects.all()

        #En este caso vamos a usar el widget checkbox multiseleccionable.

        #---------------------------------------------------------------

        self.fields["modelo"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

        self.fields["modelo"].help_text = "Seleccione el modelo a ingresar"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["modelo"].queryset = Modelo.objects.all()


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('marca1',)


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ('modelo1',)