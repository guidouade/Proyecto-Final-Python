from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post (models.Model):
    titulo=models.CharField(max_length = 60)
    subtitulo=models.CharField(max_length = 200)
    imagen=models.ImageField(upload_to='fotos', null=True, blank=True)
    contenido=models.CharField (max_length=2300)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__ (self):
        return self.titulo