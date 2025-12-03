from django.urls import path
from .views import crear_articulo

urlpatterns = [
    path('crear/', crear_articulo, name='crear_articulo'),
]
import apps.post.views as views

app_name = "post"

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name="post-list"),
]
