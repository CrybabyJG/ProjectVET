from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from apps.seguridad.usuarios.models import Usuarios
@admin.register(Usuarios)
class UsuariosAdmin(UserAdmin):
    pass