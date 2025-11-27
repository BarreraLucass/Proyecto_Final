from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta

# --- DATOS DE PRUEBA (MOCK DATA) ---
# Esto simula lo que te devolvería la base de datos.
# Puedes editar esto para probar textos largos, imágenes, etc.

NOTICIAS_FAKE = [
    {
        'id': 1,
        'titulo': 'El equipo local gana el campeonato',
        'contenido': 'Fue un partido increíble donde la hinchada no paró de alentar...',
        'categoria': {'id': 1, 'nombre': 'Deportes'},
        'fecha_publicacion': '27 Nov 2025',
        'imagen': None, # Si tienes una url de imagen ponla aquí: '/static/img/foto.jpg'
        'es_importante': True,
        'likes': 120
    },
    {
        'id': 2,
        'titulo': 'Nuevas tecnologías en 2026',
        'contenido': 'La inteligencia artificial sigue avanzando a pasos agigantados...',
        'categoria': {'id': 2, 'nombre': 'Tecnología'},
        'fecha_publicacion': '26 Nov 2025',
        'imagen': None,
        'es_importante': False,
        'likes': 45
    },
    {
        'id': 3,
        'titulo': 'Festival de música en la ciudad',
        'contenido': 'Los mejores artistas se reúnen este fin de semana...',
        'categoria': {'id': 3, 'nombre': 'Cultura'},
        'fecha_publicacion': '25 Nov 2025',
        'imagen': None,
        'es_importante': False,
        'likes': 300
    },
     {
        'id': 4,
        'titulo': 'Noticia Importante de Relleno',
        'contenido': 'Texto de prueba para ver el diseño...',
        'categoria': {'id': 1, 'nombre': 'General'},
        'fecha_publicacion': '20 Nov 2025',
        'imagen': None,
        'es_importante': True,
        'likes': 10
    }
]

CATEGORIAS_FAKE = [
    {'id': 1, 'nombre': 'Deportes'},
    {'id': 2, 'nombre': 'Tecnología'},
    {'id': 3, 'nombre': 'Cultura'},
    {'id': 4, 'nombre': 'Economía'},
]

# --- VISTAS ---

def home(request):
    # Simulación de filtros
    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q')
    
    noticias = NOTICIAS_FAKE

    # Filtro fake por categoría
    if categoria_id:
        noticias = [n for n in noticias if n['categoria']['id'] == int(categoria_id)]
    
    # Filtro fake por búsqueda
    if busqueda:
        noticias = [n for n in noticias if busqueda.lower() in n['titulo'].lower()]

    # Dividimos para el diseño (Top 3 y el resto)
    noticias_top = noticias[:3]
    noticias_destacadas = [n for n in noticias if n['es_importante']]

    context = {
        'noticias_top': noticias_top,
        'noticias_destacadas': noticias_destacadas,
        'categorias': CATEGORIAS_FAKE,
    }
    return render(request, 'index.html', context)

def detalle_noticia(request, pk):
    # 1. Buscar la noticia en la lista falsa comparando el ID
    # Usamos 'next' para encontrar el primer diccionario que coincida con el ID
    noticia_encontrada = next((n for n in NOTICIAS_FAKE if n['id'] == pk), None)

    # Si no encuentra nada (por si pones un ID raro en la url), vuelve al home
    if not noticia_encontrada:
        return redirect('home')

    ahora = timezone.now()
    
    comentarios_fake = [
        {
            'usuario': {'username': 'UsuarioDemo'}, 
            'texto': '¡Muy buena nota!', 
            'fecha': ahora - timedelta(hours=1) # Hace 1 hora real
        },
        {
            'usuario': {'username': 'Anónimo'}, 
            'texto': 'Interesante punto de vista.', 
            'fecha': ahora - timedelta(hours=3) # Hace 3 horas reales
        },
    ]

    context = {
        'noticia': noticia_encontrada, # Pasamos la noticia encontrada
        'total_likes': noticia_encontrada['likes'],
        'liked': False, 
        'comentarios': comentarios_fake,
        'form': None
    }
    return render(request, 'detalle.html', context)

def dar_like(request, pk):
    # Como no hay base de datos, no guardamos nada.
    # Solo redirigimos de vuelta a la noticia.
    return redirect('detalle_noticia', pk=pk)