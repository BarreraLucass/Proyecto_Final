from django.urls import path
import apps.categorias.views as view

app_name = 'categorias'

urlpatterns = [
    path('categorias/',view.CategoriasView.as_view(), name='categorias')
]
