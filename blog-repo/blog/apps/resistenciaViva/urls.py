from django.urls import path
from .views import *

app_name = "resistenciaViva"

urlpatterns = [
    path("crear/", CreateArticuloView.as_view(), name="create-articulos"),
    path("listar/", ListArticuloView.as_view(), name="articulos-list"),
    path("likes/", ReviewArticuloView.as_view(), name="review-articulos"),
    path("articulos/", ArticuloDetailView.as_view(), name="articulos-detail"),

]