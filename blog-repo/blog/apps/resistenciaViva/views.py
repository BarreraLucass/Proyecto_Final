from django.views.generic import TemplateView, CreateView, UpdateView


class CreateArticuloView(TemplateView):
    template_name = "resistenciaViva/create-articulos.html"


class ListArticuloView(TemplateView):
    template_name = "resistenciaViva/articulos-list.html"


# class UserUpdateView(UpdateView):
class ReviewArticuloView(TemplateView):
    template_name = "resistenciaViva/review-articulos.html"

class ArticuloDetailView(TemplateView):
    template_name = "resistenciaViva/articulos-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["articulo_id"] = pk  # para usar en el template
        return context
    
CATEGORIAS_FAKE = [
    {'id': 1, 'nombre': 'Artes Visuales', 'color': '#07151d'}, 
    {'id': 2, 'nombre': 'Musica y Cine',  'color': '#ea7300'}, 
    {'id': 3, 'nombre': 'Teatros',        'color': '#702007'}, 
    {'id': 4, 'nombre': 'Eventos',        'color': '#08525e'}, 
]

NOTICIAS_FAKE = [
    {
        'id': 1,
        'titulo': 'El equipo local gana el campeonato',
        'contenido': 'Fue un partido increíble donde la hinchada no paró de alentar...',
        'categoria': {'id': 1, 'nombre': 'ArtesVisuales'},
        'fecha_publicacion': '27 Nov 2025',
        'imagen': 'public/puro_disenio1.jpg',
        'es_importante': True,
        'likes': 120
    },
    {
        'id': 2,
        'titulo': 'Nuevas tecnologías en 2026',
        'contenido': 'La inteligencia artificial sigue avanzando...',
        'categoria': {'id': 2, 'nombre': 'TecnoMusicaCinelogía'},
        'fecha_publicacion': '26 Nov 2025',
        'imagen': 'public/imagen2.jpg',
        'es_importante': False,
        'likes': 45
    },
    {
        'id': 3,
        'titulo': 'Festival de música en la ciudad',
        'contenido': 'Los mejores artistas se reúnen...',
        'categoria': {'id': 3, 'nombre': 'CuTeatrostura'},
        'fecha_publicacion': '25 Nov 2025',
        'imagen': 'public/imagen3.jpg',
        'es_importante': False,
        'likes': 300
    },
    {
        'id': 4,
        'titulo': 'Noticia Importante de Relleno',
        'contenido': 'Texto de prueba...',
        'categoria': {'id': 4, 'nombre': 'Eventos'},
        'fecha_publicacion': '20 Nov 2025',
        'imagen': 'public/imagen4.jpg',
        'es_importante': True,
        'likes': 10
    }
]