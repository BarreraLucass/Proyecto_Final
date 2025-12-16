# from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
# #from django.http import JsonResponse
# #from django.core.mail import EmailMessage
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
# from django.contrib import messages
# from django.utils import timezone
# from datetime import timedelta


# # NOTICIAS_FAKE = [
# #     {
# #         'id': 1,
# #         'titulo': 'El equipo local gana el campeonato',
# #         'contenido': 'Fue un partido increíble...',
# #         'categoria': {'id': 1, 'nombre': 'ArtesVisuales', 'color': '#07151d'},
# #         'fecha_publicacion': '27 Nov 2025',
# #         'imagen': {'url': '/static/public/puro_disenio1.jpg'}, 
# #         'es_importante': True,
# #         'likes': 120
# #     },
# #     {
# #         'id': 2,
# #         'titulo': 'Nuevas tecnologías en 2026',
# #         'contenido': 'La inteligencia artificial...',
# #         'categoria': {'id': 2, 'nombre': 'Musica y Cine', 'color': '#ea7300'},
# #         'fecha_publicacion': '26 Nov 2025',
# #         'imagen': {'url': '/static/public/imagen2.jpg'},
# #         'es_importante': False,
# #         'likes': 45
# #     },
# #     {
# #         'id': 3,
# #         'titulo': 'Festival de música en la ciudad',
# #         'contenido': 'Los mejores artistas...',
# #         'categoria': {'id': 3, 'nombre': 'Teatros', 'color': '#702007'},
# #         'fecha_publicacion': '25 Nov 2025',
# #         'imagen': {'url': '/static/public/imagen3.jpg'},
# #         'es_importante': False,
# #         'likes': 300
# #     },
# #      {
# #         'id': 4,
# #         'titulo': 'Noticia Importante de Relleno',
# #         'contenido': 'Texto de prueba...',
# #         'categoria': {'id': 4, 'nombre': 'Eventos', 'color': '#08525e'},
# #         'fecha_publicacion': '20 Nov 2025',
# #         'imagen': {'url': '/static/public/imagen4.jpg'},
# #         'es_importante': True,
# #         'likes': 10
# #     }
# # ]

# # CATEGORIAS_FAKE = [
# #     {'id': 1, 'nombre': 'Cultura', 'color': '#07151d'}, 
# #     {'id': 2, 'nombre': 'Deportes',  'color': '#ea7300'}, 
# #     {'id': 3, 'nombre': 'Teatros',        'color': '#702007'}, 
# #     {'id': 4, 'nombre': 'Eventos',        'color': '#08525e'}, 
# # ]
# # def home(request):
# #     categoria_id = request.GET.get('categoria')
# #     busqueda = request.GET.get('q')
    
# #     noticias = NOTICIAS_FAKE
# #     color_actual = '#E85D45' 

# #     if categoria_id:
# #         categoria_id = int(categoria_id)
# #         noticias = [n for n in noticias if n['categoria']['id'] == categoria_id]
        
# #         cat_obj = next((c for c in CATEGORIAS_FAKE if c['id'] == categoria_id), None)
# #         if cat_obj:
# #             color_actual = cat_obj['color']

# #     if busqueda:
# #         noticias = [n for n in noticias if busqueda.lower() in n['titulo'].lower()]

# #     noticias_top = noticias  
    
# #     context = {
# #         'noticias_top': noticias_top,
# #         'categorias': CATEGORIAS_FAKE,
# #         'color_activo': color_actual,
# #     }
   
# #     return render(request, 'core/index.html', context)

# # def detalle_noticia(request, pk):
# #     noticia_encontrada = next((n for n in NOTICIAS_FAKE if n['id'] == pk), None)

# #     if not noticia_encontrada:
# #         return redirect('core:index')
    

# #     ahora = timezone.now()
# #     comentarios_fake = [
# #         {
# #             'usuario': {'username': 'UsuarioDemo'}, 
# #             'texto': '¡Muy buena nota!', 
# #             'fecha_creacion': ahora - timedelta(hours=1) 
# #         },
# #         {
# #             'usuario': {'username': 'Anónimo'}, 
# #             'texto': 'Interesante punto de vista.', 
# #             'fecha_creacion': ahora - timedelta(hours=3) 
# #         },
# #     ]

# #     context = {
# #         'noticia': noticia_encontrada, 
# #         'total_likes': noticia_encontrada['likes'],
# #         'liked': False, 
# #         'comentarios': comentarios_fake,
# #     }
  
# #     return render(request, 'resistenciaViva/articulos-detail.html', context)

# # def dar_like(request, pk):
   
# #     return redirect('core:detalle_noticia', pk=pk)
# # class AboutView(TemplateView):
# #     template_name = "core/about.html"


# class ContactView(TemplateView):
#     template_name = "core/contact.html"


# class NotFoundView(TemplateView):
#     template_name = "core/errors/not-found.html"


# class ServerErrorView(TemplateView):
#     template_name = "core/errors/internal-error.html"


# def custom_404(request, exception=None):
#     return render(request, "core/errors/not-found.html", status=404)


# def custom_500(request):
#     return render(request, "core/errors/internal-error.html", status=500)


# def contact_send(request):
#     if request.method != "POST":
#         return redirect(
#             "core:contact"
#         )  # Redirige a la página de contacto si no es POST

#     name = request.POST.get("name", "").strip()
#     email = request.POST.get("email", "").strip()
#     subject = request.POST.get("subject", "").strip()
#     message = request.POST.get("message", "").strip()

#     if not all([name, email, subject, message]):
#         messages.error(request, "Todos los campos son obligatorios")
#         return redirect("core:contact")

#     try:
#         validate_email(email)
#     except ValidationError:
#         messages.error(request, "El email no es válido")
#         return redirect("core:contact")

#     # # Armar mensaje
#     # body = f"""
#     # Nuevo mensaje de contacto

#     # Nombre: {name}
#     # Email: {email}
#     # Asunto: {subject}

#     # Mensaje:
#     # {message}
#     # """

#     # try:
#     #     mail = EmailMessage(
#     #         subject=f"[resistencia_viva] {subject}",
#     #         body=body,
#     #         from_email="noreply@gmail.com",  # Cambiar según config
#     #         to=["andasaber@gmail.com"],  # Adonde recibirlo
#     #         reply_to=[email],
#     #     )
#     #     mail.send()
#     # except Exception as e:
#     #     return JsonResponse({"success": False, "error": "Error al enviar email"})

#     messages.success(request, "Mensaje enviado correctamente")
#     return redirect("core:contact")


from django.shortcuts import render
from apps.post.models import Articulo
from apps.categorias.models import Categoria
from django.views.generic import TemplateView
from django.http import HttpResponse


def home(request):
    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q')

    # Traemos todos los artículos reales
    noticias = Articulo.objects.all().order_by('-fecha')

    # Filtrar por categoría si viene en la URL
    if categoria_id:
        noticias = noticias.filter(categoria_id=categoria_id)

    # Filtrar por búsqueda
    if busqueda:
        noticias = noticias.filter(titulo__icontains=busqueda)

    context = {
        'noticias_top': noticias,
        'categorias': Categoria.objects.all(),
        'color_activo': '#E85D45',  # color para probar nomas
    }

    return render(request, 'core/index.html', context)


# Página de contacto
class ContactView(TemplateView):
    template_name = "core/contact.html"


# Procesar envío del formulario de contacto
def contact_send(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        # Acá podrías enviar un email real si querés
        print("Nuevo mensaje:", nombre, email, mensaje)

        return render(request, "core/contacto_exito.html")

    return HttpResponse("Método no permitido", status=405)


# Página “Acerca de”
class AboutView(TemplateView):
    template_name = "core/about.html"


# Página 404 personalizada
class NotFoundView(TemplateView):
    template_name = "core/404.html"


# Página 500 personalizada
class ServerErrorView(TemplateView):
    template_name = "core/500.html"




