from django.shortcuts import render, get_object_or_404
from .models import Categoria
from apps.post.models import Articulo

def articulos_por_categoria(request, slug): 
    categoria = get_object_or_404(Categoria, slug=slug) # Obtenes la categoría o devolver 404 si no existe
    articulos = Articulo.objects.filter(categoria=categoria).order_by("-fecha") # Filtras los artículos por categoría
    return render(request, "articulos_por_categoria.html", {
        "categoria": categoria,
        "articulos": articulos,
    })

def lista_categorias(request): 
    categorias = Categoria.objects.all() # Obtienes todas las categorías
    return render(request, "categorias/categorias.html", {"categorias": categorias})