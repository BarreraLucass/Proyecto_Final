from apps.categorias.models import Categoria

def categorias_context(request):
    return {
        "categorias": Categoria.objects.all()
    }
