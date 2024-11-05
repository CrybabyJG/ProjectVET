from rest_framework.serializers import ModelSerializer, CharField
from .models import Cita, Detalle_Cita


class DetalleCitaSerializer(ModelSerializer):
    Nombre_enfermedad = CharField(source='ID_Enfermedades.Descripcion', read_only=True)
    class Meta:
        model = Detalle_Cita
        fields = ['Codigo_DetalleCita', 'Descripcion', 'ID_Enfermedades', 'Nombre_enfermedad']

class CitaSerializer(ModelSerializer):
    Estado_cita = CharField(source='ID_EstadoCita.Descripcion', read_only=True)
    Nombre_mascota = CharField(source='ID_Mascota.Nombre_Mascota', read_only=True)
    detalles = DetalleCitaSerializer(many=True)
    class Meta:
        model = Cita
        fields = ['Codigo_Cita', 'Fecha_de_Cita', 'Peso', 'ID_EstadoCita', 'Estado_cita', 'ID_Mascota',
                  'Nombre_mascota', 'detalles']