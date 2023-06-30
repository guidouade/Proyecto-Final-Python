from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormularioSugerencias, FormularioSugerenciasUpdate
from .models import Sugerencia
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

#def sugerencia (request):
#      if request.method == 'POST':
#            miFormulario = FormularioSugerencias(request.POST) # Aqui me llega la informacion del html
#            print(miFormulario)
#            if miFormulario.is_valid():
#                  informacion = miFormulario.cleaned_data
#                  sugerir= Sugerencia(nombre=informacion['nombre'], email=informacion['email'], sugerencia=informacion['sugerencia'])
#                  sugerir.save()
#                  return render(request, "ProyectoFinalApp/inicio.html")
#      else:
#            miFormulario = FormularioSugerencias()
#      return render(request,"sugerencia/miFormulario.html", {"miFormulario":miFormulario})

@login_required
def sugerencia_list(request):
    sugerencias = Sugerencia.objects.all()
    return render(request, 'sugerencia/sugerencia_list.html', {'sugerencias': sugerencias})

@login_required
def sugerencia_create(request):
    if request.method == 'POST':
        form = FormularioSugerencias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sugerencia-list')
    else:
        form = FormularioSugerencias()
    form = FormularioSugerencias()
    return render(request, 'sugerencia/sugerencia_create.html', {'form': form})

@login_required
def sugerencia_update(request, pk):
    sugerencia = get_object_or_404(Sugerencia, pk=pk)
    if request.method == 'POST':
        form = FormularioSugerenciasUpdate(request.POST, instance=sugerencia)
        if form.is_valid():
            form.save()
            return redirect('sugerencia-list')
    else:
        form = FormularioSugerenciasUpdate(instance=sugerencia)
    return render(request, 'sugerencia/sugerencia_update.html', {'form': form, 'sugerencia': sugerencia})

@login_required
def sugerencia_delete(request, pk):
    sugerencia = get_object_or_404(Sugerencia, pk=pk)
    if request.method == 'POST':
        sugerencia.delete()
        return redirect('sugerencia-list')
    return render(request, 'sugerencia/sugerencia_delete.html')


def password_exitoso(request):
    return render(request, 'ProyectoFinalApp/passwordExitoso.html', {})