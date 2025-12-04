from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): # se define qué columnas se ven en la lista del admin
    list_display = ("nombre", "slug") 
    search_fields = ("nombre",) 
    prepopulated_fields = {"slug": ("nombre",)} # el campo slug se autocompleta con el nombre
# ejemplo: si el nombre es "Tecnología", el slug será "tecnologia" osea si tiene mayusculas o tildes o espacios no importa