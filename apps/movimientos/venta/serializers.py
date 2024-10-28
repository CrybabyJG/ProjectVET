from rest_framework.serializers import ModelSerializer, CharField
from .models import Venta, DetalleVenta

class DetalleVentaSerializer(ModelSerializer):
    medicamento_name = CharField(source='ID_Medicamento.Descripcion', read_only=True)
    class Meta:
        model = DetalleVenta
        fields = ['ID_Medicamento', 'medicamento_name', 'Cantidad']

class VentaSerializer(ModelSerializer):
    cliente_name = CharField(source='ID_Cliente.Nombres', read_only=True)
    detalles = DetalleVentaSerializer(many=True)
    class Meta:
        model = Venta
        fields = ['Codigo_Venta', 'ID_Cliente', 'cliente_name', 'Descripcion', 'detalles']