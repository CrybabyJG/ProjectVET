from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Raza
from .serializers import RazaSerializer
from drf_yasg.utils import swagger_auto_schema

class RazaAPIView(APIView):
    """
    Vista para listar todas las razas o crear una nueva raza.
    """

    @swagger_auto_schema(responses={200: RazaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las razas.
        """
        razas = Raza.objects.all()
        serializer = RazaSerializer(razas, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RazaSerializer, responses={201: RazaSerializer})
    def post(self, request):
        """
        Crear una nueva raza.
        """
        serializer = RazaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RazaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una raza específica.
    """

    @swagger_auto_schema(responses={200: RazaSerializer})
    def get(self, request, pk):
        """
        Obtener una raza específica por su ID.
        """
        try:
            raza = Raza.objects.get(pk=pk)
        except Raza.DoesNotExist:
            return Response({'error': 'Raza no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RazaSerializer(raza)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RazaSerializer, responses={200: RazaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente una raza por su ID.
        """
        try:
            raza = Raza.objects.get(pk=pk)
        except Raza.DoesNotExist:
            return Response({'error': 'Raza no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RazaSerializer(raza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=RazaSerializer, responses={200: RazaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una raza por su ID.
        """
        try:
            raza = Raza.objects.get(pk=pk)
        except Raza.DoesNotExist:
            return Response({'error': 'Raza no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RazaSerializer(raza, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una raza por su ID.
        """
        try:
            raza = Raza.objects.get(pk=pk)
        except Raza.DoesNotExist:
            return Response({'error': 'Raza no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        raza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)