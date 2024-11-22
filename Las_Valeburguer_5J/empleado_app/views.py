from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.

def inicio_vista(request):
    losempleados=Empleado.objects.all()
    return render(request,"gestionarEmpleado.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]

    guardarempleado=Empleado.objects.create(
        codigo=codigo,
        nombre=nombre,
        credito=credito
    )# GUARDA EL REGISTRO

    return redirect ("/")

def seleccionarEmpleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    return render(request,"editarempleado.html",{"misempleados": empleado})

def editarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]
    empleado=Empleado.objects.get(codigo=codigo)
    empleado.nombre=nombre
    empleado.credito=credito
    empleado.save() #guarda registro actualizado
    return redirect("/")

def borrarEmpleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    empleado.delete() # borra el registro
    return redirect ("/")