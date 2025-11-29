from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta


NOTICIAS_FAKE = [
    {
        'id': 1,
        'titulo': 'El equipo local gana el campeonato',
        'contenido': 'Fue un partido increíble donde la hinchada no paró de alentar...',
        'categoria': {'id': 1, 'nombre': 'ArtesVisuales'},
        'fecha_publicacion': '27 Nov 2025',
        'imagen': None, 
        'es_importante': True,
        'likes': 120
    },
    {
        'id': 2,
        'titulo': 'Nuevas tecnologías en 2026',
        'contenido': 'La inteligencia artificial sigue avanzando a pasos agigantados...',
        'categoria': {'id': 2, 'nombre': 'TecnoMusicaCinelogía'},
        'fecha_publicacion': '26 Nov 2025',
        'imagen': None,
        'es_importante': False,
        'likes': 45
    },
    {
        'id': 3,
        'titulo': 'Festival de música en la ciudad',
        'contenido': 'Los mejores artistas se reúnen este fin de semana...',
        'categoria': {'id': 3, 'nombre': 'CuTeatrostura'},
        'fecha_publicacion': '25 Nov 2025',
        'imagen': None,
        'es_importante': False,
        'likes': 300
    },
     {
        'id': 4,
        'titulo': 'Noticia Importante de Relleno',
        'contenido': 'Texto de prueba para ver el diseño...',
        'categoria': {'id': 4, 'nombre': 'Eventos'},
        'fecha_publicacion': '20 Nov 2025',
        'imagen': None,
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

def home(request):
    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q')
    
    noticias = NOTICIAS_FAKE

    color_actual = '#E85D45' 

    if categoria_id:
        categoria_id = int(categoria_id)
        noticias = [n for n in noticias if n['categoria']['id'] == categoria_id]
        
        cat_obj = next((c for c in CATEGORIAS_FAKE if c['id'] == categoria_id), None)
        if cat_obj:
            color_actual = cat_obj['color']

    
    if busqueda:
        noticias = [n for n in noticias if busqueda.lower() in n['titulo'].lower()]

    noticias_top = noticias[:3]
    noticias_destacadas = [n for n in noticias if n['es_importante']]

    context = {
        'noticias_top': noticias_top,
        'noticias_destacadas': noticias_destacadas,
        'categorias': CATEGORIAS_FAKE,
        'color_activo': color_actual,
    }
    return render(request, 'index.html', context)

def detalle_noticia(request, pk):
    noticia_encontrada = next((n for n in NOTICIAS_FAKE if n['id'] == pk), None)

    if not noticia_encontrada:
        return redirect('home')
    
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
        'form': None
    }
    return render(request, 'detalle.html', context)

def dar_like(request, pk):
    return redirect('detalle_noticia', pk=pk)