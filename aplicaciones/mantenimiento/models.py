from django.db import models

# Create your models here.

#TABLAS
class Impresora(models.Model):
    ESTADO_CHOICES = [
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ]

    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    propietario = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='en_proceso')

    def __str__(self):
        return f"{self.marca} - {self.propietario} ({self.estado})"




