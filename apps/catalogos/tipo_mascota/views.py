from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TipoMascota
from .serializers import TipoMascotaSerializer
from drf_yasg.utils import swagger_auto_schema

class TipoMascotaAPIView(APIView):
    """
    Vista para listar todos los tipos de mascota o crear un nuevo tipo de mascota.
    """

    @swagger_auto_schema(responses={200: TipoMascotaSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los tipos de mascota.
        """
        tipos_mascota = TipoMascota.objects.all()
        serializer = TipoMascotaSerializer(tipos_mascota, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoMascotaSerializer, responses={201: TipoMascotaSerializer})
    def post(self, request):
        """
        Crear un nuevo tipo de mascota.
        """
        serializer = TipoMascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoMascotaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un tipo de mascota específico.
    """

    @swagger_auto_schema(responses={200: TipoMascotaSerializer})
    def get(self, request, pk):
        """
        Obtener un tipo de mascota específico por su ID.
        """
        try:
            tipo_mascota = TipoMascota.objects.get(pk=pk)
        except TipoMascota.DoesNotExist:
            return Response({'error': 'Tipo de mascota no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TipoMascotaSerializer(tipo_mascota)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoMascotaSerializer, responses={200: TipoMascotaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un tipo de mascota por su ID.
        """
        try:
            tipo_mascota = TipoMascota.objects.get(pk=pk)
        except TipoMascota.DoesNotExist:
            return Response({'error': 'Tipo de mascota no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoMascotaSerializer(tipo_mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TipoMascotaSerializer, responses={200: TipoMascotaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un tipo de mascota por su ID.
        """
        try:
            tipo_mascota = TipoMascota.objects.get(pk=pk)
        except TipoMascota.DoesNotExist:
            return Response({'error': 'Tipo de mascota no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoMascotaSerializer(tipo_mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un tipo de mascota por su ID.
        """
        try:
            tipo_mascota = TipoMascota.objects.get(pk=pk)
        except TipoMascota.DoesNotExist:
            return Response({'error': 'Tipo de mascota no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        tipo_mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)