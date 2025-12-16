from django.views.generic import TemplateView


class ComentariosView(TemplateView):
    template_name = 'comentarios/comentarios.html'