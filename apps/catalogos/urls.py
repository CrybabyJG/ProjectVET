from django.urls import path, include

urlpatterns = [
    path('enfermedades/', include('apps.catalogos.enfermedades.urls')),
    path('estado_de_cita/', include('apps.catalogos.estado_de_cita.urls')),
    path('mascota/', include('apps.catalogos.mascota.urls')),
    path('presentacion/', include('apps.catalogos.presentacion.urls')),
    path('raza/', include('apps.catalogos.raza.urls')),
    path('tipo_mascota/', include('apps.catalogos.tipo_mascota.urls')),
    path('unidad_medida/', include('apps.catalogos.unidad_medida.urls')),

]