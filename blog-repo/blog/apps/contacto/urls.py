from django.urls import path
from .views import contacto_view

urlpatterns = [
    path("", contacto_view, name="apps.contacto.urls.contacto_view"),
]
