from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, unique=True) 
    descripcion = models.TextField(blank=True, null=True) #texto opcional para describir la categoria
    slug = models.SlugField(unique=True) # El slug es como el "alias" que se usa en la URL 

    def __str__(self):  
        return self.nombre  

    class Meta:
        ordering = ["nombre"] 
        # Estos nombres son los que se muestran en el admin
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"