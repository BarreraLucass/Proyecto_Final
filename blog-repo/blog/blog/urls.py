from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.view import IndexView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home
    path('', include("apps.core.urls", namespace='core')),

    # rutas principales
    path('post/', include('apps.post.urls', namespace='post')),
    path('user/', include('apps.user.urls', namespace='user')),
    path("login/", auth_views.LoginView.as_view(template_name="auth/auth-login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="core:index"), name="logout"),
    path('comentarios/', include('apps.comentarios.urls', namespace='comentarios')),
    path('categorias/', include('apps.categorias.urls', namespace='categorias')),
    path('resistencia/', include('apps.resistenciaViva.urls', namespace='resistenciaViva')),
    path('contacto/', include("apps.contacto.urls")),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)