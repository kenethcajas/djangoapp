from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import VehiculoForm, MarcaForm, ModeloForm
from proyfinvehiculos.models import Vehiculo, Marca, Modelo
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





def vehiculo_nuevo(request):
    if request.method == "POST":
        formulario = VehiculoForm(request.POST,request.FILES)
        if formulario.is_valid():

            for marca_id in request.POST.getlist('marca'):
                for modelo_id in request.POST.getlist('modelo'):
                    fecha = timezone.now()
                    vehiculo = Vehiculo(fecha_ingreso=fecha,marca_id=marca_id,modelo_id=modelo_id,imagen=request.FILES)
                    formulario.save()
                    return redirect('proyfinvehiculos.views.vehiculo_lista')
                    messages.add_message(request, messages.SUCCESS, 'Vehiculo Guardado Exitosamente')

    else:
        formulario = VehiculoForm()
    return render(request, 'proyfinvehiculos/vehiculo_nuevo.html', {'formulario': formulario})


@login_required

def vehiculo_lista(request):
    vehiculos = Vehiculo.objects.filter(fecha_ingreso=timezone.now()).order_by('fecha_ingreso')
    return render(request, 'proyfinvehiculos/vehiculo_lista.html', {'vehiculos':vehiculos})

def vehiculo_detalle(request, pk):
    post = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'proyfinvehiculos/vehiculo_detalle.html', {'post':post})

def vehiculo_editar(request, pk):
    vehiculos = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        formulario = VehiculoForm(request.POST,request.FILES, instance=vehiculos)
        if formulario.is_valid():
            for marca_id in request.POST.getlist('marca'):
                for modelo_id in request.POST.getlist('modelo'):
                    fecha = timezone.now()
                    vehiculo = Vehiculo(fecha_ingreso=fecha,marca_id=marca_id,modelo_id=modelo_id,imagen=request.FILES)
                    formulario.save()
                    #return render(request, 'proyfinvehiculos/vehiculo_lista.html', {'vehiculos':vehiculos})
                    return redirect('proyfinvehiculos/vehiculo_lista.html', pk=vehiculo.pk)
                    messages.add_message(request, messages.SUCCESS, 'Vehiculo Guardado Exitosamente')

    else:
        formulario = VehiculoForm(instance=vehiculos)
    return render(request, 'proyfinvehiculos/vehiculo_editar.html', {'formulario': formulario})
    


def vehiculo_eliminar(request, pk):
    post = get_object_or_404(Vehiculo, pk=pk)
    post.delete()
    return redirect('proyfinvehiculos/vehiculo_lista.html', pk=vehiculo.pk)


def marca_nueva(request):
    if request.method == "POST":
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            marca = formulario.save(commit=False)
            marca.save()
            return redirect('proyfinvehiculos.views.marca_lista')
    else:
        formulario = MarcaForm()
    return render(request, 'proyfinvehiculos/marca_nueva.html', {'formulario': formulario})

def marca_lista(request):
    marca = Marca.objects.all 
    return render(request, 'proyfinvehiculos/marca_lista.html', {'marca':marca})

def marca_detalle(request, pk):
    post = get_object_or_404(Marca, pk=pk)
    return render(request, 'proyfinvehiculos/marca_detalle.html', {'post':post})

def marca_editar(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            marca = formulario.save(commit=False)
            marca.save()
            return redirect('proyfinvehiculos.views.marca_detalle', pk=marca.pk)
    else:
        formulario = MarcaForm()
    return render(request, 'proyfinvehiculos/marca_editar.html', {'formulario': formulario})
    
    


def marca_eliminar(request, pk):
    post = get_object_or_404(Marca, pk=pk)
    post.delete()
    return redirect('proyfinvehiculos/marca_lista.html', pk=post.pk)





def modelo_nuevo(request):
    if request.method == "POST":
        formulario = ModeloForm(request.POST)
        if formulario.is_valid():
            modelo = formulario.save(commit=False)
            modelo.save()
            return redirect('proyfinvehiculos.views.modelo_lista')
    else:
        formulario = ModeloForm()
    return render(request, 'proyfinvehiculos/modelo_nuevo.html', {'formulario': formulario})

def modelo_lista(request):
    modelo = Modelo.objects.all 
    return render(request, 'proyfinvehiculos/modelo_lista.html', {'modelo':modelo})

def modelo_detalle(request, pk):
    post = get_object_or_404(Modelo, pk=pk)
    return render(request, 'proyfinvehiculos/modelo_detalle.html', {'post':post})

def modelo_editar(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == "POST":
        formulario = ModeloForm(request.POST)
        if formulario.is_valid():
            modelo = formulario.save(commit=False)
            modelo.save()
            return redirect('proyfinvehiculos.views.modelo_detalle', pk=modelo.pk)
    else:
        formulario = ModeloForm()
    return render(request, 'proyfinvehiculos/modelo_editar.html', {'formulario': formulario})
    
    


def modelo_eliminar(request, pk):
    post = get_object_or_404(Modelo, pk=pk)
    post.delete()
    return redirect('proyfinvehiculos/modelo_lista.html', pk=post.pk)

    