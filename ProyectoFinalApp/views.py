from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.edit import UpdateView, FormView 
from fototeca.models import Post
from recuerdos.models import Caja
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import FormularioCambioPassword, FormularioEdicion, FormularioRegistroUsuario


# Create your views here.

def inicio (request):
    return render (request, "ProyectoFinalApp/inicio.html")

def busqueda_fototecas (request):
    return render (request, "fotos/busqueda_fototecas.html")

def buscar (request):
    if request.GET["fttc"]:
        mensaje= "Fototeca buscada: %r" %request.GET["fttc"]
        fototeca=request.GET["fttc"]
        fotos=Post.objects.filter (titulo__icontains=fototeca)
        return render (request, "fotos/resultados_busqueda.html", {"fotos":fotos, "query":fototeca})
    else:
        mensaje="No introdujiste nada"

    return HttpResponse(mensaje)

def busqueda_recuerdos (request):
    return render (request, "caja/busqueda_recuerdos.html")

def buscar_recuerdo (request):
    if request.GET["fttc"]:
        mensaje= "Recuerdo buscado: %r" %request.GET["fttc"]
        caja=request.GET["fttc"]
        recuerdos=Caja.objects.filter (titulo__icontains=caja)
        return render (request, "caja/resultados_busqueda.html", {"recuerdos":recuerdos, "query":caja})
    else:
        mensaje="No introdujiste nada"

    return HttpResponse(mensaje)

class LoginPagina(LoginView):
    template_name = 'ProyectoFinalApp/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')

class RegistroPagina(FormView):
    template_name = 'ProyectoFinalApp/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'ProyectoFinalApp/edicionPerfil.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'ProyectoFinalApp/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'ProyectoFinalApp/passwordExitoso.html', {})