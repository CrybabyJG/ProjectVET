from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Presentacion
from .serializers import PresentacionSerializer
from drf_yasg.utils import swagger_auto_schema

class PresentacionAPIView(APIView):
    """
    Vista para listar todas las presentaciones o crear una nueva presentación.
    """

    @swagger_auto_schema(responses={200: PresentacionSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las presentaciones.
        """
        presentaciones = Presentacion.objects.all()
        serializer = PresentacionSerializer(presentaciones, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PresentacionSerializer, responses={201: PresentacionSerializer})
    def post(self, request):
        """
        Crear una nueva presentación.
        """
        serializer = PresentacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PresentacionDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una presentación específica.
    """

    @swagger_auto_schema(responses={200: PresentacionSerializer})
    def get(self, request, pk):
        """
        Obtener una presentación específica por su ID.
        """
        try:
            presentacion = Presentacion.objects.get(pk=pk)
        except Presentacion.DoesNotExist:
            return Response({'error': 'Presentación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PresentacionSerializer(presentacion)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PresentacionSerializer, responses={200: PresentacionSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una presentación por su ID.
        """
        try:
            presentacion = Presentacion.objects.get(pk=pk)
        except Presentacion.DoesNotExist:
            return Response({'error': 'Presentación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PresentacionSerializer(presentacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PresentacionSerializer, responses={200: PresentacionSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una presentación por su ID.
        """
        try:
            presentacion = Presentacion.objects.get(pk=pk)
        except Presentacion.DoesNotExist:
            return Response({'error': 'Presentación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PresentacionSerializer(presentacion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una presentación por su ID.
        """
        try:
            presentacion = Presentacion.objects.get(pk=pk)
        except Presentacion.DoesNotExist:
            return Response({'error': 'Presentación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        presentacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)