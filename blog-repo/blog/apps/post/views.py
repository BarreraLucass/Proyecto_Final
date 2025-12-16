from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect,  get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Articulo, Categoria
from apps.comentarios.forms import ComentarioForm


# Lista de artículos
class ArticuloListView(ListView):
    model = Articulo
    template_name = "post/post-list.html"
    context_object_name = "articulos"
    ordering = ['-fecha_publicacion']


# DETALLE + COMENTARIOS, Dios ayudame por favor (soy ateo)
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "post/detalle_articulo.html"
    context_object_name = "articulo"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articulo = self.get_object()

        context["comentarios"] = articulo.comentarios.filter(activo=True)
        context["form"] = ComentarioForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.articulo = self.object
            nuevo_comentario.usuario = request.user
            nuevo_comentario.save()

        return redirect("post:detalle_articulo", slug=self.object.slug)


# Crear artículo (solo usuarios logueados)
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = "post/post-new.html"
    fields = ['titulo', 'contenido', 'imagen', 'categoria']
    success_url = reverse_lazy('post:lista_articulos')


# Editar artículo (solo usuarios logueados)
class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    template_name = "post/post-update.html"
    fields = ['titulo', 'contenido', 'imagen', 'categoria']
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse_lazy('post:detalle_articulo', kwargs={'slug': self.object.slug})


# Eliminar artículo (solo usuarios logueados)
class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = "post/post-delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy('post:lista_articulos')

# Vista para filtrar artículos por categoría

def articulos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    articulos = Articulo.objects.filter(categoria=categoria)
    return render(request, 'post/articulos-list.html', {
        'categoria': categoria,
        'articulos': articulos
    })
