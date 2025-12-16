from django.urls import path
from .views import (
    ArticuloListView,
    ArticuloDetailView,
    ArticuloCreateView,
    ArticuloUpdateView,
    ArticuloDeleteView,
    articulos_por_categoria,
)

app_name = 'post'

urlpatterns = [
    path('categoria/<slug:slug>/', articulos_por_categoria, name='categoria'),
    path('', ArticuloListView.as_view(), name='lista_articulos'),
    path('nuevo/', ArticuloCreateView.as_view(), name='nuevo_articulo'),
    path('<slug:slug>/', ArticuloDetailView.as_view(), name='detalle_articulo'),
    path('<slug:slug>/editar/', ArticuloUpdateView.as_view(), name='editar_articulo'),
    path('<slug:slug>/eliminar/', ArticuloDeleteView.as_view(), name='eliminar_articulo'),
]