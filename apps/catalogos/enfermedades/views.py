from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enfermedades
from .serializers import EnfermedadesSerializer
from drf_yasg.utils import swagger_auto_schema

class EnfermedadesAPIView(APIView):
    """
    Vista para listar todas las enfermedades o crear una nueva enfermedad.
    """

    @swagger_auto_schema(responses={200: EnfermedadesSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las enfermedades.
        """
        enfermedades = Enfermedades.objects.all()
        serializer = EnfermedadesSerializer(enfermedades, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EnfermedadesSerializer, responses={201: EnfermedadesSerializer})
    def post(self, request):
        """
        Crear una nueva enfermedad.
        """
        serializer = EnfermedadesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnfermedadesDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una enfermedad específica.
    """

    @swagger_auto_schema(responses={200: EnfermedadesSerializer})
    def get(self, request, pk):
        """
        Obtener una enfermedad específica por su ID.
        """
        try:
            enfermedad = Enfermedades.objects.get(pk=pk)
        except Enfermedades.DoesNotExist:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EnfermedadesSerializer(enfermedad)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EnfermedadesSerializer, responses={200: EnfermedadesSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una enfermedad por su ID.
        """
        try:
            enfermedad = Enfermedades.objects.get(pk=pk)
        except Enfermedades.DoesNotExist:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EnfermedadesSerializer(enfermedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=EnfermedadesSerializer, responses={200: EnfermedadesSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una enfermedad por su ID.
        """
        try:
            enfermedad = Enfermedades.objects.get(pk=pk)
        except Enfermedades.DoesNotExist:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EnfermedadesSerializer(enfermedad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una enfermedad por su ID.
        """
        try:
            enfermedad = Enfermedades.objects.get(pk=pk)
        except Enfermedades.DoesNotExist:
            return Response({'error': 'Enfermedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        enfermedad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)