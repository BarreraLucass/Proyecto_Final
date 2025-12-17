from django.shortcuts import get_object_or_404, redirect
from .models import Comentario
from django.contrib.auth.decorators import login_required

@login_required
def responder_comentario(request, comentario_id):
    padre = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Comentario.objects.create(
                usuario=request.user,
                contenido=contenido,
                articulo=padre.articulo,
                parent=padre
            )
    return redirect('post:detalle_articulo', slug=padre.articulo.slug)

@login_required
def like_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.user in comentario.likes.all():
        comentario.likes.remove(request.user)
    else:
        comentario.likes.add(request.user)
    return redirect('post:detalle_articulo', slug=comentario.articulo.slug)