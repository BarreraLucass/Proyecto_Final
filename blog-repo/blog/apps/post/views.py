from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from apps.comentarios.forms import ComentarioForm

def detalle_articulo(request, slug):
    # Buscamos el artículo por su slug (alias en la URL)
    articulo = get_object_or_404(Articulo, slug=slug)

    # Traemos los comentarios activos de ese artículo
    comentarios = articulo.comentarios.filter(activo=True)

    # Si el usuario envió el formulario (POST)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.articulo = articulo
            nuevo_comentario.usuario = request.user
            nuevo_comentario.save()
            return redirect("detalle_articulo", slug=articulo.slug)
    else:
        form = ComentarioForm()
    
    return render(request, "post/post-detail.html", {
        "articulo": articulo,
        "comentarios": comentarios,
        "form": form
    })