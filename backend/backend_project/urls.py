
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('loops.urls')), # ruta prueba
    #path('api/', include('loops.urls')),  # Incluir las rutas de la API
]
