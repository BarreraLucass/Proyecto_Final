from django.urls import path
from .views import crear_articulo

urlpatterns = [
    path('crear/', crear_articulo, name='crear_articulo'),
]
