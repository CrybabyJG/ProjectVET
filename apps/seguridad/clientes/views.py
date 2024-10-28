from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Clientes
from .serializers import ClientesSerializer
from drf_yasg.utils import swagger_auto_schema

class ClientesViewSet(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente para los clientes.
    """

    @swagger_auto_schema(responses={200: ClientesSerializer(many=True)})
    def list(self, request):
        """
        Devuelve la lista de todos los clientes.
        """
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        Devuelve un cliente específico por ID.
        """
        try:
            cliente = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientesSerializer(cliente)
        return Response(serializer.data)

    def create(self, request):
        """
        Crea un nuevo cliente.
        """
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """
        Actualiza completamente un cliente existente.
        """
        try:
            cliente = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientesSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        """
        Actualización parcial de un cliente.
        """
        try:
            cliente = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientesSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Elimina un cliente existente.
        """
        try:
            cliente = Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)