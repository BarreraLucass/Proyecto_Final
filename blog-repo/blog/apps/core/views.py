from django.shortcuts import render, redirect
from django.views.generic import TemplateView
#from django.http import JsonResponse
#from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render
from apps.core.data import CATEGORIAS_FAKE, NOTICIAS_FAKE

class IndexView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class NotFoundView(TemplateView):
    template_name = "core/errors/not-found.html"


class ServerErrorView(TemplateView):
    template_name = "core/errors/internal-error.html"


def custom_404(request, exception=None):
    return render(request, "core/errors/not-found.html", status=404)


def custom_500(request):
    return render(request, "core/errors/internal-error.html", status=500)


def contact_send(request):
    if request.method != "POST":
        return redirect(
            "core:contact"
        )  # Redirige a la página de contacto si no es POST

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()

    if not all([name, email, subject, message]):
        messages.error(request, "Todos los campos son obligatorios")
        return redirect("core:contact")

    try:
        validate_email(email)
    except ValidationError:
        messages.error(request, "El email no es válido")
        return redirect("core:contact")

    # # Armar mensaje
    # body = f"""
    # Nuevo mensaje de contacto

    # Nombre: {name}
    # Email: {email}
    # Asunto: {subject}

    # Mensaje:
    # {message}
    # """

    # try:
    #     mail = EmailMessage(
    #         subject=f"[resistencia_viva] {subject}",
    #         body=body,
    #         from_email="noreply@gmail.com",  # Cambiar según config
    #         to=["andasaber@gmail.com"],  # Adonde recibirlo
    #         reply_to=[email],
    #     )
    #     mail.send()
    # except Exception as e:
    #     return JsonResponse({"success": False, "error": "Error al enviar email"})

    messages.success(request, "Mensaje enviado correctamente")
    return redirect("core:contact")

def home_final(request):
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

    return render(request, 'core/index.html', context)