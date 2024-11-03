from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CitaSerializer, DetalleCitaSerializer
from .models import Cita, Detalle_Cita, Mascota, EstadodeCita, Enfermedades
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction


class CitaAPIView(APIView):
    @swagger_auto_schema(responses={200: CitaSerializer()})
    def get(self, request, pk=None):
        cita = Cita.objects.all()
        serializer = CitaSerializer(cita, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CitaSerializer)
    def post(self, request):
        serializer = CitaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Crea la instancia de Cita con los datos validados
                    estado_cita = get_object_or_404(EstadodeCita,
                                                    pk=serializer.validated_data['ID_EstadoCita'].ID_EstadoCita)
                    mascota = get_object_or_404(Mascota, pk=serializer.validated_data['ID_Mascota'].ID_Mascota)

                    cita = Cita.objects.create(
                        Codigo_Cita=serializer.validated_data['Codigo_Cita'],
                        Fecha_de_Cita=serializer.validated_data['Fecha_de_Cita'],
                        Peso=serializer.validated_data['Peso'],
                        ID_EstadoCita=estado_cita,
                        ID_Mascota=mascota
                    )

                    # Procesa cada detalle en los datos validados
                    for detalle_data in serializer.validated_data['detalles']:
                        enfermedad = get_object_or_404(Enfermedades, pk=detalle_data['ID_Enfermedades'].ID_Enfermedades)
                        Detalle_Cita.objects.create(
                            Codigo_DetalleCita=detalle_data['Codigo_DetalleCita'],
                            Descripcion=detalle_data['Descripcion'],
                            ID_Enfermedades=enfermedad,
                            ID_Cita=cita
                        )

                cita_serializer = CitaSerializer(cita)
                return Response(cita_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Cita_Detalle_details(APIView):
    @swagger_auto_schema(responses={200: CitaSerializer()})
    def get(self, request, pk):
        # Obtiene la cita por ID
        cita = get_object_or_404(Cita, pk=pk)
        serializer = CitaSerializer(cita)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        cita = get_object_or_404(Cita, pk=pk)
        try:
            with transaction.atomic():
                # Elimina primero los detalles relacionados con la cita
                Detalle_Cita.objects.filter(ID_Cita=cita).delete()
                # Luego, elimina la cita
                cita.delete()

            return Response({"message": "Cita eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)