from django.urls import path
from .views import lista_categorias, articulos_por_categoria

app_name = 'categorias'

urlpatterns = [
    path("categorias/", lista_categorias, name="lista_categorias"),
    path("categoria/<slug:slug>/", articulos_por_categoria, name="articulos_por_categoria"),
]