from rest_framework.serializers import ModelSerializer, CharField
from .models import Medicamento, DetalleMedicamento

class DetalleMedicamentoSerializer(ModelSerializer):
    cita_code = CharField(source='ID_Cita.Codigo_Cita', read_only=True)
    class Meta:
        model = DetalleMedicamento
        fields = ['ID_Cita', 'cita_code', 'Cantidad', 'Descripcion']

class MedicamentoSerializer(ModelSerializer):
    presentacion_name = CharField(source='ID_Presentacion.Peso', read_only=True)
    unidad_medida_name = CharField(source='ID_Unidad_Medida.Descripcion', read_only=True)
    detalles = DetalleMedicamentoSerializer(many=True)
    class Meta:
        model = Medicamento
        fields = ['Codigo_Medicamento', 'Descripcion', 'Precio', 'ID_Presentacion', 'presentacion_name', 'ID_Unidad:Medida',
                  'unidad_medida_name', 'detalles']