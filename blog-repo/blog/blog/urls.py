from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views

from apps.core.views import home_final  # Home de la maqueta + real
from apps.post.views import detalle_noticia, dar_like


urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME 
    path('', home_final, name='home'),

    # APPS
    path('core/', include('apps.core.urls', namespace='core')),
    path('user/', include('apps.user.urls', namespace='user')),
    path('comentarios/', include('apps.comentarios.urls', namespace='comentarios')),
    path('post/', include('apps.post.urls', namespace='post')),
    path('categorias/', include('apps.categorias.urls', namespace='categorias')),
    path('resistencia/', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),
    path('contacto/', include('apps.contacto.urls')),
    path('noticia/<int:pk>/', detalle_noticia, name='detalle_noticia'),
    path('noticia/<int:pk>/like/', dar_like, name='dar_like'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
