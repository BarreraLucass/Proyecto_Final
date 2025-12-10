from django.urls import path
from .views import detalle_articulo

app_name = 'post'

urlpatterns = [
    path('articulo/<slug:slug>/', detalle_articulo, name='detalle_articulo'),
] 