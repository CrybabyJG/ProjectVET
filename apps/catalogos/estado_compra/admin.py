from django.contrib import admin

from apps.catalogos.estado_compra.models import EstadodeCompra

# Register your models here.
@admin.register(EstadodeCompra)
class EstadodeCompraAdmin(admin.ModelAdmin):
    search_fields = ['Codigo_EstadoCompra', 'Descripcion']
    list_display = ['Codigo_EstadoCompra', 'Descripcion']