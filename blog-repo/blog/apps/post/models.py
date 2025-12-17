from django.db import models
from django.conf import settings
from apps.categorias.models import Categoria
from django.utils.text import slugify

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=10000)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articulos', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.likes.count()