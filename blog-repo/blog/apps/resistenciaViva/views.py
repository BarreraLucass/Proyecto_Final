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

class ContactoView(TemplateView):
    template_name = "resistenciaViva/contacto.html"

class AcercaDeNosotrosView(TemplateView):
    template_name = "resistenciaViva/acerca-de-nosotros.html"