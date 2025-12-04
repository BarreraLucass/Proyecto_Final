
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.view import IndexView

#Seguir con las rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path('', include('apps.user.urls')),
    path('', include('apps.comentarios.urls', namespace='comentarios')),
    path('', include('apps.post.urls', namespace='post')),
    path('', include('apps.categorias.urls', namespace='categorias')),
    path('', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),
]



if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)