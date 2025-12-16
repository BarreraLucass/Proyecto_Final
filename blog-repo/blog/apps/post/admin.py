from django.contrib import admin
from .models import Articulo

# Probando admin
# admin.site.register(Articulo)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha', 'total_likes')
    list_filter = ('categoria', 'fecha', 'autor')
    search_fields = ('titulo', 'contenido', 'autor__username')
    readonly_fields = ('likes',)

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = 'Cantidad de likes'