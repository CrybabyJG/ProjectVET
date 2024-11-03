from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VentaSerializer
from .models import Venta, DetalleVenta, Clientes, Medicamento
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction


class VentaAPIView(APIView):
    @swagger_auto_schema(responses={200: VentaSerializer()})
    def get(self, request, pk=None):
        venta = get_object_or_404(Venta, pk=pk)
        serializer = VentaSerializer(venta)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        # Inicializa el serializer con los datos del request
        serializer = VentaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # Inicia una transacción atómica
                with transaction.atomic():
                    # Obtiene el cliente usando el ID proporcionado en los datos validados
                    cliente = get_object_or_404(Clientes, pk=serializer.validated_data['ID_Cliente'].ID_Cliente)

                    # Crea la instancia de Venta
                    venta = Venta.objects.create(
                        Codigo_Venta=serializer.validated_data['Codigo_Venta'],
                        ID_Cliente=cliente,
                        Descripcion=serializer.validated_data['Descripcion']
                    )

                    # Procesa cada detalle en los datos validados
                    for detalle_data in serializer.validated_data['detalles']:
                        cantidad = detalle_data['Cantidad']
                        # Obtiene el medicamento relacionado o devuelve 404 si no existe
                        medicamento = get_object_or_404(Medicamento, pk=detalle_data['ID_Medicamento'].ID_Medicamento)
                        preciototal = medicamento.Precio * cantidad
                        # Crea el detalle de la venta con la información relevante
                        DetalleVenta.objects.create(
                            ID_Venta=venta,
                            ID_Medicamento=medicamento,
                            Cantidad=cantidad,
                            Precio=preciototal  # Asigna el precio del medicamento actual
                        )

                # Serializa la venta con los detalles incluidos para la respuesta
                venta_serializer = VentaSerializer(venta)
                return Response(venta_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Devuelve un error en caso de excepción
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Devuelve errores de validación si los datos no son válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Venta_Detalle_details(APIView):
    @swagger_auto_schema(responses={200: VentaSerializer()})
    def get(self, request, pk):
        # Obtiene la venta por ID
        venta = get_object_or_404(Venta, pk=pk)
        serializer = VentaSerializer(venta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    @swagger_auto_schema(request_body=VentaSerializer)
    def patch(self, request, pk):
        venta = get_object_or_404(Venta, pk=pk)
        serializer = VentaSerializer(venta, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    if 'ID_Cliente' in serializer.validated_data:
                        cliente = get_object_or_404(Clientes, pk=serializer.validated_data['ID_Cliente'].ID_Cliente)
                        venta.ID_Cliente = cliente

                    venta.Codigo_Venta = serializer.validated_data.get('Codigo_Venta', venta.Codigo_Venta)
                    venta.Descripcion = serializer.validated_data.get('Descripcion', venta.Descripcion)
                    venta.save()

                    if 'detalles' in serializer.validated_data:
                        for detalle_data in serializer.validated_data['detalles']:
                            detalle_id = detalle_data.get('ID_DetalleVenta')
                            detalle_venta = get_object_or_404(DetalleVenta, pk=detalle_id)
                            detalle_venta.Cantidad = detalle_data.get('Cantidad', detalle_venta.Cantidad)
                            medicamento = get_object_or_404(Medicamento,
                                                            pk=detalle_data['ID_Medicamento'].ID_Medicamento)
                            detalle_venta.ID_Medicamento = medicamento
                            detalle_venta.Precio = medicamento.Precio * detalle_venta.Cantidad
                            detalle_venta.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=VentaSerializer)
    def put(self, request, pk):
        venta = get_object_or_404(Venta, pk=pk)
        serializer = VentaSerializer(venta, data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    cliente = get_object_or_404(Clientes, pk=serializer.validated_data['ID_Cliente'].ID_Cliente)
                    venta.ID_Cliente = cliente
                    venta.Codigo_Venta = serializer.validated_data['Codigo_Venta']
                    venta.Descripcion = serializer.validated_data['Descripcion']
                    venta.save()

                    DetalleVenta.objects.filter(ID_Venta=venta).delete()
                    for detalle_data in serializer.validated_data['detalles']:
                        medicamento = get_object_or_404(Medicamento, pk=detalle_data['ID_Medicamento'].ID_Medicamento)
                        DetalleVenta.objects.create(
                            ID_Venta=venta,
                            ID_Medicamento=medicamento,
                            Cantidad=detalle_data['Cantidad'],
                            Precio=medicamento.Precio * detalle_data['Cantidad']
                        )

                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

    def delete(self, request, pk=None):
        # Busca la venta específica por su ID
        venta = get_object_or_404(Venta, pk=pk)

        try:
            # Usa una transacción para asegurar que la eliminación sea atómica
            with transaction.atomic():
                # Elimina primero los detalles relacionados
                DetalleVenta.objects.filter(ID_Venta=venta).delete()

                # Luego, elimina la venta
                venta.delete()

            return Response({"message": "Venta eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            # Devuelve un error detallado en caso de falla
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
