from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EstadodeCita
from .serializers import EstadodeCitaSerializer
from drf_yasg.utils import swagger_auto_schema

class EstadodeCitaAPIView(APIView):
    """
    Vista para listar todos los estados de citas o crear un nuevo estado de cita.
    """

    @swagger_auto_schema(responses={200: EstadodeCitaSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los estados de citas.
        """
        estados_cita = EstadodeCita.objects.all()
        serializer = EstadodeCitaSerializer(estados_cita, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EstadodeCitaSerializer, responses={201: EstadodeCitaSerializer})
    def post(self, request):
        """
        Crear un nuevo estado de cita.
        """
        serializer = EstadodeCitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstadodeCitaDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un estado de cita específico.
    """

    @swagger_auto_schema(responses={200: EstadodeCitaSerializer})
    def get(self, request, pk):
        """
        Obtener un estado de cita específico por su ID.
        """
        try:
            estado_cita = EstadodeCita.objects.get(pk=pk)
        except EstadodeCita.DoesNotExist:
            return Response({'error': 'Estado de cita no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EstadodeCitaSerializer(estado_cita)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EstadodeCitaSerializer, responses={200: EstadodeCitaSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un estado de cita por su ID.
        """
        try:
            estado_cita = EstadodeCita.objects.get(pk=pk)
        except EstadodeCita.DoesNotExist:
            return Response({'error': 'Estado de cita no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EstadodeCitaSerializer(estado_cita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=EstadodeCitaSerializer, responses={200: EstadodeCitaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un estado de cita por su ID.
        """
        try:
            estado_cita = EstadodeCita.objects.get(pk=pk)
        except EstadodeCita.DoesNotExist:
            return Response({'error': 'Estado de cita no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EstadodeCitaSerializer(estado_cita, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un estado de cita por su ID.
        """
        try:
            estado_cita = EstadodeCita.objects.get(pk=pk)
        except EstadodeCita.DoesNotExist:
            return Response({'error': 'Estado de cita no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        estado_cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)