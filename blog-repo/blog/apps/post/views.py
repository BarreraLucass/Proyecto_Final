from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ArticuloForm
from .models import Articulo, Comentario

@login_required
@permission_required('posts.add_articulo', raise_exception=True)
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.slug = articulo.titulo.replace(" ", "-").lower()
            articulo.save()
            return redirect('detalle_articulo', slug=articulo.slug)
    else:
        form = ArticuloForm()
    return render(request, 'posts/crear_articulo.html', {'form': form})

@login_required
@permission_required('posts.change_articulo', raise_exception=True)
def editar_articulo(request, slug):
    articulo = Articulo.objects.get(slug=slug)

    if request.user != articulo.autor and not request.user.is_staff:
        return redirect('home')

    form = ArticuloForm(request.POST or None, request.FILES or None, instance=articulo)

    if form.is_valid():
        form.save()
        return redirect('detalle_articulo', slug=slug)

    return render(request, 'posts/editar_articulo.html', {'form': form, 'articulo': articulo})

@login_required
@permission_required('posts.delete_articulo', raise_exception=True)
def eliminar_articulo(request, slug):
    articulo = Articulo.objects.get(slug=slug)
    articulo.delete()
    return redirect('home')

@login_required
def crear_comentario(request, slug):
    articulo = Articulo.objects.get(slug=slug)
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        Comentario.objects.create(
            articulo=articulo,
            usuario=request.user,
            contenido=contenido
        )
    return redirect('detalle_articulo', slug=slug)

@login_required
def editar_comentario(request, id):
    comentario = Comentario.objects.get(id=id)

    if request.user != comentario.usuario:
        return redirect('home')

    if request.method == 'POST':
        comentario.contenido = request.POST.get('contenido')
        comentario.save()
        return redirect('detalle_articulo', slug=comentario.articulo.slug)
    return render(request, 'posts/editar_comentario.html', {'comentario': comentario})

@login_required
def eliminar_comentario(request, id):
    comentario = Comentario.objects.get(id=id)
    
    if request.user == comentario.usuario or request.user.is_staff:
        comentario.delete()

    return redirect('detalle_articulo', slug=comentario.articulo.slug)
