# loops/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('loops/', views.test_view, name='test_view'),  # Ruta para datos de prueba
]
