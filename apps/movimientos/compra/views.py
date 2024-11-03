from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompraSerializer
from .models import Compra, DetalleCompra, Medicamento
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction

class CompraAPIView(APIView):
    @swagger_auto_schema(responses={200: CompraSerializer()})
    def get(self, request, pk=None):
        compra = get_object_or_404(Compra, pk=pk)
        serializer = CompraSerializer(compra)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=CompraSerializer)
    def post(self, request):
        # Inicializa el serializer con los datos del request
        serializer = CompraSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # Inicia una transacción atómica
                with transaction.atomic():
                    # Obtiene el proveedor usando el ID proporcionado en los datos validados
                    #proveedor = get_object_or_404(Proveedores, pk=serializer.validated_data['ID_Proveedor'].ID_Proveedor)
                    #El codigo de arriba sera modificado si se agrega un Proveedor

                    # Crea la instancia de Venta
                    compra = Compra.objects.create(
                        Codigo_Compra=serializer.validated_data['Codigo_Compra'],
                        #ID_Proveedor=proveedor,
                        Descripcion=serializer.validated_data['Descripcion']
                    )

                    # Procesa cada detalle en los datos validados
                    for detalle_data in serializer.validated_data['detalles']:
                        cantidad = detalle_data['Cantidad']
                        # Obtiene el medicamento relacionado o devuelve 404 si no existe
                        medicamento = get_object_or_404(Medicamento, pk=detalle_data['ID_Medicamento'].ID_Medicamento)
                        preciototal = medicamento.Precio * cantidad
                        # Crea el detalle de la venta con la información relevante
                        DetalleCompra.objects.create(
                            ID_Compra=compra,
                            ID_Medicamento=medicamento,
                            Cantidad=cantidad,
                            Precio=preciototal  # Asigna el precio del medicamento actual
                        )

                # Serializa la venta con los detalles incluidos para la respuesta
                compra_serializer = CompraSerializer(compra)
                return Response(compra_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Devuelve un error en caso de excepción
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Devuelve errores de validación si los datos no son válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Compra_Detalle_details(APIView):
    @swagger_auto_schema(responses={200: CompraSerializer()})
    def get(self, request, pk):
        # Obtiene la compra por ID
        compra = get_object_or_404(Compra, pk=pk)
        serializer = CompraSerializer(compra)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        # Busca la compra específica por su ID
        compra = get_object_or_404(Compra, pk=pk)
        try:
            # Usa una transacción para asegurar que la eliminación sea atómica
            with transaction.atomic():
                # Elimina primero los detalles relacionados
                DetalleCompra.objects.filter(ID_Compra=compra).delete()
                # Luego, elimina la compra
                compra.delete()

            return Response({"message": "Compra eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            # Devuelve un error detallado en caso de falla
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)