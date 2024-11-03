from django.urls import path
from .views import CompraAPIView, Compra_Detalle_details

app_name = 'compra'

urlpatterns = [
    path("", CompraAPIView.as_view(), name="compra"),
    path("<int:pk>/", Compra_Detalle_details.as_view()),
]