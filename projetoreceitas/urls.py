from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('aplicativoreceitas.urls')),
    path('usuarios/', include('aplicativousuarios.urls')),
    path('airlines/', include('aplicativoairlines.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
