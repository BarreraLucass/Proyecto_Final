from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.view import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas principales
    path('', include("apps.core.urls", namespace='core')),  # Home

    # Rutas con prefijo
    path('user/', include('apps.user.urls', namespace='user')),
    path('post/', include('apps.post.urls', namespace='post')),
    path('categorias/', include('apps.categorias.urls', namespace='categorias')),
    path('resistencia/', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),
    path('contacto/', include("apps.contacto.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('comentarios/', include('apps.comentarios.urls', namespace='comentarios')),
]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
