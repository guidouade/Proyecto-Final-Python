from django.shortcuts import render
from nosotros.models import Nosotros

# Create your views here.

def nosotros (request):
    nosotros = Nosotros.objects.all()
    return render (request, "nosotros/nosotros.html", {"nosotros":nosotros})

def password_exitoso(request):
    return render(request, 'ProyectoFinalApp/passwordExitoso.html', {})