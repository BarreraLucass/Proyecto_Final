from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('responder/<int:comentario_id>/', views.responder_comentario, name='responder'),
    path('like/<int:comentario_id>/', views.like_comentario, name='like'),
]