from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.view import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),

    path('', include("apps.core.urls", namespace='core')),
    path('', include('apps.user.urls', namespace='user')),
    path('', include('apps.comentarios.urls', namespace='comentarios')),
    path('', include('apps.post.urls', namespace='post')),
    path('', include('apps.categorias.urls', namespace='categorias')),
    path('', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),
    path('', include('apps.core.urls')),
    path("contacto/", include("apps.contacto.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)