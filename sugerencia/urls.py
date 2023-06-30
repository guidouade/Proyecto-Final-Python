from django.urls import path
from . import views
from ProyectoFinalApp.views import LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginPagina.as_view(), name='login'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(template_name='ProyectoFinalApp/logout.html'), name='logout'),
    path('editarperfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('cambiarpassword/', CambioPassword.as_view(), name='cambiar_password'),

    path('',views.sugerencia_list, name='sugerencia-list'),
    path('create/',views.sugerencia_create, name='sugerencia-create'),
    path('<pk>/update/',views.sugerencia_update, name='sugerencia-update'),
    path('<pk>/delete/',views.sugerencia_delete, name='sugerencia-delete'),
]