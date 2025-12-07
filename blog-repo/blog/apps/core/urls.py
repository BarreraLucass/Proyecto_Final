from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
   path('', home, name='index'),
    path('detalle/<int:pk>/', detalle_noticia, name='detalle_noticia'),
    path('detalle/<int:pk>/like/', dar_like, name='dar_like'),
    path("contacto/", ContactView.as_view(), name="contact"),
    path("acerca-de/", AboutView.as_view(), name="about"),
    path("404/", NotFoundView.as_view(), name="404"),
    path("500/", ServerErrorView.as_view(), name="500"),
    path("contact/send/", contact_send, name="contact_send"),
]