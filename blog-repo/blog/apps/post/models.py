from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.articulo}"