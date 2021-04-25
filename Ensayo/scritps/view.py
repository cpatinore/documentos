from django.shortcuts import render, HttpResponse

def home(request):
    getoutput("cd raiz")
    ubicacion= getoutput("pwd")

    return render(request, "index.html",{"ubicacion": ubicacion})

def crear(request):
    return render(request,"Crear.html")

def borrar(request):
    return render(request,"Borrar.html")

