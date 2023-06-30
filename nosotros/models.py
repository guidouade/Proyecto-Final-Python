from django.db import models

# Create your models here.

class Nosotros (models.Model):
    titulo=models.CharField(max_length = 60)
    contenido=models.CharField(max_length = 500)
    imagen=models.ImageField(upload_to='nosotros')

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__ (self):
        return self.titulo