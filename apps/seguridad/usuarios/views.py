from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuariosSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class UsuariosAPIView(APIView):
    @swagger_auto_schema(request_body=UsuariosSerializer)
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)

        #Validar los datos
        if serializer.is_valid():
            serializer.save() #Creacion del usuario
            return Response({"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
        #En caso de error, retornar las validaciones
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)