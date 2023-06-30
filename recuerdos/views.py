from django.shortcuts import render
from recuerdos.models import Caja

# Create your views here.

def cajas (request):
    cajas = Caja.objects.all()
    return render (request, "caja/caja.html", {"cajas":cajas})

def detalles (request, id):
    detalles=Caja.objects.get (id=id)
    return render (request, "caja/posts.html", {"caja":detalles})

def password_exitoso(request):
    return render(request, 'ProyectoFinalApp/passwordExitoso.html', {})