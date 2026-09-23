from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rotas da aplicação por empresa
    path('', include('usuarios.urls')),
]

# Libera o acesso às logos enviadas durante o desenvolvimento local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)