from django.views.generic import TemplateView
from .forms import ComentarioForm 

class ComentariosView(TemplateView):
    template_name = 'comentarios/comentarios.html'