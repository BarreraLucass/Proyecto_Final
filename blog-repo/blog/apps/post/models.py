from django.db import models
from django.contrib.auth.models import User
from apps.categorias.models import Categoria

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.likes.count()