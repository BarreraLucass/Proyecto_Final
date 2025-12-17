from django.db import models
from django.conf import settings


class Comentario(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    articulo = models.ForeignKey(
        "post.Articulo",
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    #  Nuevo: comentario padre (para respuestas)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="respuestas"
    )

    #  Nuevo: likes en comentarios
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="likes_comentarios",
        blank=True
    )

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.articulo}"

    #  Saber si es un comentario principal
    def es_principal(self):
        return self.parent is None

    #  Contar likes
    def total_likes(self):
        return self.likes.count()

    # Obtener respuestas ordenadas
    def get_respuestas(self):
        return self.respuestas.filter(activo=True).order_by("fecha")


    def __str__(self):
        return f"Comentario de {self.usuario} en {self.articulo}"

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
