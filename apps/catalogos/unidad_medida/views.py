from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UnidadMedida
from .serializers import UnidadMedidaSerializer
from drf_yasg.utils import swagger_auto_schema
from apps.seguridad.permissions import CustomPermission
from rest_framework.permissions import IsAuthenticated

class UnidadMedidaAPIView(APIView):
    """
    Vista para listar todas las unidades de medida o crear una nueva unidad de medida.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = UnidadMedida

    @swagger_auto_schema(responses={200: UnidadMedidaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las unidades de medida.
        """
        unidades_medida = UnidadMedida.objects.all()
        serializer = UnidadMedidaSerializer(unidades_medida, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UnidadMedidaSerializer, responses={201: UnidadMedidaSerializer})
    def post(self, request):
        """
        Crear una nueva unidad de medida.
        """
        serializer = UnidadMedidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnidadMedidaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una unidad de medida específica.
    """

    @swagger_auto_schema(responses={200: UnidadMedidaSerializer})
    def get(self, request, pk):
        """
        Obtener una unidad de medida específica por su ID.
        """
        try:
            unidad_medida = UnidadMedida.objects.get(pk=pk)
        except UnidadMedida.DoesNotExist:
            return Response({'error': 'Unidad de medida no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UnidadMedidaSerializer(unidad_medida)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UnidadMedidaSerializer, responses={200: UnidadMedidaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una unidad de medida por su ID.
        """
        try:
            unidad_medida = UnidadMedida.objects.get(pk=pk)
        except UnidadMedida.DoesNotExist:
            return Response({'error': 'Unidad de medida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadMedidaSerializer(unidad_medida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=UnidadMedidaSerializer, responses={200: UnidadMedidaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una unidad de medida por su ID.
        """
        try:
            unidad_medida = UnidadMedida.objects.get(pk=pk)
        except UnidadMedida.DoesNotExist:
            return Response({'error': 'Unidad de medida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadMedidaSerializer(unidad_medida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una unidad de medida por su ID.
        """
        try:
            unidad_medida = UnidadMedida.objects.get(pk=pk)
        except UnidadMedida.DoesNotExist:
            return Response({'error': 'Unidad de medida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        unidad_medida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)