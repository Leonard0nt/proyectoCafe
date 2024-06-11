from django.db import models

# Create your models here.
from django.db import models

class Registro(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    TIPO_CHOICES = [
        ('Reclamo', 'Reclamo'),
        ('Felicitaciones', 'Felicitaciones'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensaje = models.TextField()

