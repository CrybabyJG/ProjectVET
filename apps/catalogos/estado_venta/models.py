from django.db import models

# Create your models here.
class EstadodeVenta(models.Model):
    ID_EstadoVenta = models.AutoField(primary_key=True)
    Codigo_EstadoVenta = models.CharField(max_length=10, verbose_name='Codigo de estado de venta')
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')

    class Meta:
        verbose_name_plural = 'Estados de ventas'

    def __str__(self):
        return f'{self.Codigo_EstadoVenta} - {self.Descripcion}'