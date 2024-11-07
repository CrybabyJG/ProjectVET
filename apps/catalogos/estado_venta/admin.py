from django.contrib import admin

from apps.catalogos.estado_venta.models import EstadodeVenta

# Register your models here.
@admin.register(EstadodeVenta)
class EstadodeVentaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_EstadoVenta', 'Descripcion']
    list_display = ['Codigo_EstadoVenta', 'Descripcion']