from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "articulo", "contenido", "fecha", "activo")
    list_filter = ("activo", "fecha", "usuario")
    search_fields = ("contenido", "usuario__username", "articulo__titulo")
