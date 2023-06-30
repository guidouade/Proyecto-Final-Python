from django.urls import path
from ProyectoFinalApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path ('', views.inicio, name= "Inicio"),

    #Login, Registro y Logout
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='ProyectoFinalApp/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('editarperfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('cambiarpassword/', CambioPassword.as_view(), name='cambiar_password'),
    path('login/registro/', RegistroPagina.as_view(), name='registro'),
    path('logout/registro/', RegistroPagina.as_view(), name='registro'),

    #Busquedas de Fototeca y Caja de Recuerdos
    path ('busqueda_recuerdos/', views.busqueda_recuerdos),
    path ('busqueda_fototecas/', views.busqueda_fototecas),
    path ('buscar/', views.buscar),
    path ('buscar_recuerdo/', views.buscar_recuerdo),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)