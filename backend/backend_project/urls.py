
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin/')),  # Redirige la raíz a /admin
    path('api/', include('loops.urls')), # ruta prueba
    #path('api/', include('loops.urls')),  # Incluir las rutas de la API
]
