from django.urls import path
import apps.comentarios.views as view

app_name = 'comentarios'

urlpatterns = [
    path('comentarios/',view.ComentariosView.as_view(), name='comentarios')
]
