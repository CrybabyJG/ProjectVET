from django.contrib import admin

from apps.movimientos.cita.models import Cita, Detalle_Cita


# Register your models here.
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_Cita']
    list_display = ['Codigo_Cita', 'Fecha_Realizacion', 'Fecha_de_Cita', 'ID_EstadoCita', 'ID_Mascota', 'Peso']

@admin.register(Detalle_Cita)
class DetalleCitaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_DetalleCita']
    list_display = ['Codigo_DetalleCita', 'Descripcion', 'ID_Enfermedades', 'ID_Cita']