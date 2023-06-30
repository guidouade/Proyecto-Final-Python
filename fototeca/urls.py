from django.urls import path
from . import views
from ProyectoFinalApp.views import LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('', views.fotos, name= "Fototeca"),
    path ('<int:id>/', views.fototeca, name= "fototeca"),
    path('login/', LoginPagina.as_view(), name='login'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(template_name='ProyectoFinalApp/logout.html'), name='logout'),
    path('editarperfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('cambiarpassword/', CambioPassword.as_view(), name='cambiar_password'),

]
