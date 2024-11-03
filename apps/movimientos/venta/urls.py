from django.urls import path
from .views import VentaAPIView , Venta_Detalle_details

app_name = 'venta'

urlpatterns = [
    path("", VentaAPIView.as_view(), name="venta"),
    path('<int:pk>/', Venta_Detalle_details.as_view())

]