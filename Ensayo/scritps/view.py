from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")