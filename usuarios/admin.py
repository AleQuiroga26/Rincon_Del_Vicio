from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    # Agregamos 'foto' a los campos que se pueden ver/editar en el admin
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('foto',)}),
    )
