from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactoForm

def contacto_view(request):
    enviado = False

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()

            # mail al usuario
            send_mail(
                subject="¡Gracias por tu mensaje!",
                message=f"Hola {mensaje.nombre},\n\nRecibimos tu mensaje y pronto nos pondremos en contacto.\n\nGracias por escribirnos.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[mensaje.email],
            )

            # mail interno opcional
            send_mail(
                subject=f"Nuevo mensaje: {mensaje.asunto}",
                message=f"Nombre: {mensaje.nombre}\nEmail: {mensaje.email}\n\nMensaje:\n{mensaje.mensaje}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            return redirect("/contacto?ok=1")

    else:
        form = ContactoForm()
        if request.GET.get("ok"):
            enviado = True

    return render(request, "contacto/contacto.html", {
        "form": form,
        "enviado": enviado
    
    })

