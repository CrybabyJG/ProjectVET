from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.mascota.models import Mascota
from .serializers import MascotaSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class MascotaAPIView(APIView):
    """
    Vista para listar todas las mascotas o crear una nueva mascota.
    """

    @swagger_auto_schema(responses={200: MascotaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las mascotas.
        """
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MascotaSerializer, responses={201: MascotaSerializer})
    def post(self, request):
        """
        Crear una nueva mascota.
        """
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una mascota específica.
    """

    @swagger_auto_schema(responses={200: MascotaSerializer})
    def get(self, request, pk):
        """
        Obtener una mascota específica por su ID.
        """
        try:
            mascota = Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MascotaSerializer, responses={200: MascotaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una mascota por su ID.
        """
        try:
            mascota = Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MascotaSerializer(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MascotaSerializer, responses={200: MascotaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una mascota por su ID.
        """
        try:
            mascota = Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MascotaSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una mascota por su ID.
        """
        try:
            mascota = Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)