from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.view import IndexView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),

    path('', include("apps.core.urls", namespace='core')),
    path('', include('apps.user.urls', namespace='user')),
    path("login/", auth_views.LoginView.as_view(template_name="auth/auth-login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="core:index"), name="logout"),
    path('', include('apps.comentarios.urls', namespace='comentarios')),
    path('', include('apps.post.urls', namespace='post')),
    path('', include('apps.categorias.urls', namespace='categorias')),
    path("contacto/", include("apps.contacto.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)