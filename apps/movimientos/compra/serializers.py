from rest_framework.serializers import ModelSerializer, CharField
from .models import Compra, DetalleCompra

class DetalleCompraSerializer(ModelSerializer):
    Nombre_Medicamento = CharField(source='ID_Medicamento.Descripcion', read_only=True)
    class Meta:
        model = DetalleCompra
        fields = ['ID_Medicamento', 'Nombre_Medicamento', 'Cantidad']

class CompraSerializer(ModelSerializer):
    detalles = DetalleCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ['Codigo_Compra', 'Descripcion', 'detalles']