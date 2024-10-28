from django.db import models
from apps.catalogos.medicamento.models import Medicamento

# Create your models here.
class Compra(models.Model):
    ID_Compra = models.AutoField(primary_key=True)
    Codigo_Compra = models.CharField(max_length=10, verbose_name='Codigo de compra', unique=True)
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    Fecha = models.DateField(verbose_name='Fecha', auto_now_add=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total')
#AQUI RELLENAR CAMPO DE PROVEEDOR MAS ADELANTE
    class Meta:
        verbose_name_plural = 'Compras'

    def __str__(self):
        return f'{self.Codigo_Compra} - {self.Descripcion}'


class DetalleCompra(models.Model):
    ID_DetalleCompra = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal')
    ID_Compra = models.ForeignKey(Compra, related_name='Detalles',on_delete=models.PROTECT)
    ID_Medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento',on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalles de Compras'

    def __str__(self):
        return f'{self.ID_DetalleCompra} - {self.ID_Compra.Codigo_Compra} - {self.ID_Medicamento}'