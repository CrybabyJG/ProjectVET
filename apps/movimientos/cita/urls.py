from django.urls import path
from .views import CitaAPIView, Cita_Detalle_details

app_name = 'cita'

urlpatterns = [
    path("", CitaAPIView.as_view(), name="cita"),
    path("<int:pk>/", Cita_Detalle_details.as_view()),
]