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


class Mantenimiento(models.Model):
    id = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField()
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE, related_name='mantenimientos')

    def __str__(self):
        return f"Mantenimiento {self.id} - {self.impresora.marca} ({self.costo} USD)"
