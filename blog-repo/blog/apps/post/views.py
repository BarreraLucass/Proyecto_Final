from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from apps.comentarios.forms import ComentarioForm
from django.utils import timezone
from datetime import timedelta



#  VISTA REAL (BASE DE DATOS)
def detalle_articulo(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug)
    comentarios = articulo.comentarios.filter(activo=True)

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

#   DATOS FAKE DEL FRONT
NOTICIAS_FAKE = [
    {
        'id': 1,
        'titulo': 'El equipo local gana el campeonato',
        'contenido': 'Fue un partido increíble...',
        'categoria': {'id': 1, 'nombre': 'ArtesVisuales'},
        'fecha_publicacion': '27 Nov 2025',
        'imagen': 'public/puro_disenio1.jpg',
        'es_importante': True,
        'likes': 120
    },
    {
        'id': 2,
        'titulo': 'Nuevas tecnologías en 2026',
        'contenido': 'La inteligencia artificial sigue...',
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
        'titulo': 'Exposición de arte contemporáneo',
        'contenido': 'Una muestra que desafía los límites...',
        'categoria': {'id': 4, 'nombre': 'EventArte'},
        'fecha_publicacion': '24 Nov 2025',
        'imagen': 'public/imagen4.jpg',
        'es_importante': True,
        'likes': 150
    },
    {
        'id': 5,
        'titulo': 'Noticia Importante de Relleno',
        'contenido': 'Texto de prueba...',
        'categoria': {'id': 4, 'nombre': 'Eventos'},
        'fecha_publicacion': '20 Nov 2025',
        'imagen': 'public/imagen5.jpg',
        'es_importante': True,
        'likes': 10
    }
]

CATEGORIAS_FAKE = [
    {'id': 1, 'nombre': 'Artes Visuales', 'color': '#07151d'}, 
    {'id': 2, 'nombre': 'Musica y Cine',  'color': '#ea7300'}, 
    {'id': 3, 'nombre': 'Teatros',        'color': '#702007'}, 
    {'id': 4, 'nombre': 'Eventos',        'color': '#08525e'}, 
]


#  VISTA "FAKE" DETALLE NOTICIA 
def detalle_noticia(request, pk):
    noticia_encontrada = next((n for n in NOTICIAS_FAKE if n['id'] == pk), None)

    if not noticia_encontrada:
        return redirect('home')

    # Obtener color de categoría
    cat_id = noticia_encontrada['categoria']['id']
    cat_obj = next((c for c in CATEGORIAS_FAKE if c['id'] == cat_id), None)

    if cat_obj:
        noticia_encontrada['categoria']['color'] = cat_obj['color']

    ahora = timezone.now()

    comentarios_fake = [
        {
            'usuario': {'username': 'UsuarioDemo'},
            'texto': '¡Muy buena nota!',
            'fecha': ahora - timedelta(hours=1)
        },
        {
            'usuario': {'username': 'Anónimo'},
            'texto': 'Interesante punto de vista.',
            'fecha': ahora - timedelta(hours=3)
        },
    ]

    context = {
        'noticia': noticia_encontrada,
        'total_likes': noticia_encontrada['likes'],
        'liked': False,
        'comentarios': comentarios_fake,
        'form': None,
    }

    return render(request, 'detalle.html', context)


#  LIKE FAKE del mockup de Carla
def dar_like(request, pk):
    return redirect("detalle_noticia", pk=pk)

