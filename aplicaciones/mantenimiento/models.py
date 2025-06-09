from django.db import models

# Create your models here.

#TABLAS




class Mantenimiento(models.Model):
    id = models.AutoField(primary_key=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField()
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE, related_name='mantenimientos')

    def __str__(self):
        return f"Mantenimiento {self.id} - {self.impresora.marca} ({self.costo} USD)"
