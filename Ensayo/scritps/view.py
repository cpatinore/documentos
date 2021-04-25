from django.shortcuts import render
import os
from subprocess import *
from django import forms

inicio = True
principalub= ""

def home(request):
    global inicio
    global principalub
    if inicio:
        ubicacion= getoutput("pwd")
        principalub=ubicacion
        path= ubicacion + "/raiz"
        os.chdir(path)
    ubicacion= getoutput("pwd")
    return render(request, "index.html",{"ubicacion": ubicacion})

def crear(request):
    tipo= request.GET("tipo")
    nombre= request.GET("nombre")
    return render(request,"Crear.html")

def borrar(request):
    return render(request,"Borrar.html")

def copiar(request):
    return render(request,"copiar.html")

def renombrar(request):
    return render(request,"Renombrar.html")

def mover(request):
    return render(request,"Mover.html")

def verPermisos(request):
    return render(request,"VerPermisos.html")

def cambiarPermisos(request):
    return render(request,"CambiarPermisos.html")

def cambiarPropietario(request):
    return render(request,"CambiarPropietario.html")

