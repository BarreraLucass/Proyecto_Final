from django.urls import path
from .views import *

app_name = "resistenciaViva"

urlpatterns = [
    path("escuela/crear/", CreateArticuloView.as_view(), name="create-articulos"),
    path("escuela/listar/", ListArticuloView.as_view(), name="articulos-list"),
    path("escuela/calificar/", ReviewArticuloView.as_view(), name="review-articulos"),
    path("escuela/<int:pk>/", ArticuloDetailView.as_view(), name="articulos-detail"),

]