from django.shortcuts import render
from fototeca.models import Post

# Create your views here.

def fotos (request):
    posts = Post.objects.all()
    return render (request, "fotos/fototeca.html", {"posts":posts})

def fototeca (request, id):
    fototeca=Post.objects.get (id=id)
    return render (request, "fotos/posts.html", {"post":fototeca})

def password_exitoso(request):
    return render(request, 'ProyectoFinalApp/passwordExitoso.html', {})