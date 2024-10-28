from django.urls import path
from .views import UsuariosAPIView

urlpatterns = [
    path("", UsuariosAPIView.as_view(), name="usuarios"),
]