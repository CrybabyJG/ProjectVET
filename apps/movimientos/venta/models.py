from django.db import models
from apps.seguridad.clientes.models import Clientes
from apps.catalogos.medicamento.models import Medicamento
# Create your models here.
class Venta(models.Model):
    ID_Venta = models.AutoField(primary_key=True)
    Codigo_Venta = models.CharField(max_length=10, verbose_name='Codigo de venta', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    Fecha = models.DateField(verbose_name='Fecha', auto_now_add=True)
    ID_Cliente = models.ForeignKey(Clientes, verbose_name='Nombre del cliente', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f'{self.Codigo_Venta} - {self.Fecha}'


class DetalleVenta(models.Model):
    ID_DetalleVenta = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    Precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    ID_Venta = models.ForeignKey(Venta, related_name='Detalles', on_delete=models.PROTECT)
    ID_Medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalles de ventas'

    def __str__(self):
        return f'{self.Venta.Codigo_Venta} - {self.ID_Medicamento}'