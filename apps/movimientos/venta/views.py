from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VentaSerializer
from .models import Venta, DetalleVenta, Clientes, Medicamento
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction


class VentaAPIView(APIView):
    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Obtener el cliente a partir del ID en los datos validados
                    cliente = get_object_or_404(Clientes, pk=serializer.validated_data['ID_Cliente'].ID_Cliente)

                    # Crear la venta
                    venta = Venta.objects.create(
                        Codigo_Venta=serializer.validated_data['Codigo_Venta'],
                        ID_Cliente=cliente,
                        Descripcion=serializer.validated_data['Descripcion']
                    )

                    # Iterar sobre los detalles
                    for detalle_data in serializer.validated_data['detalles']:
                        cantidad = detalle_data['Cantidad']
                        medicamento = get_object_or_404(Medicamento, pk=detalle_data['ID_Medicamento'].ID_Medicamento)

                        # Crear el detalle de la venta
                        DetalleVenta.objects.create(
                            ID_Venta=venta,
                            ID_Medicamento=medicamento,
                            Cantidad=cantidad,
                            Precio=medicamento.Precio  # Asignar el precio del medicamento
                        )

                # Serializar la venta con los detalles incluidos
                venta_serializer = VentaSerializer(venta)
                return Response(venta_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
