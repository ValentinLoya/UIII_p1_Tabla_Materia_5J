from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarCliente.html",{"misclientes":losclientes})

def registrarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]

    guardarmateria=Cliente.objects.create(
        codigo=codigo,
        nombre=nombre,
        credito=credito
    )# GUARDA EL REGISTRO

    return redirect ("/")

def seleccionarCliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    return render(request,"editarcliente.html",{"misclientes": cliente})

def editarCliente(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.nombre=nombre
    cliente.credito=credito
    cliente.save() #guarda registro actualizado
    return redirect("/")

def borrarCliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.delete() # borra el registro
    return redirect ("/")