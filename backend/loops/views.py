from django.shortcuts import render
from django.http import JsonResponse

def test_view(request):
    # Datos de prueba que se enviarán como respuesta JSON
    sample_data = [
        {"id": 1, "title": "Loop 1", "description": "Descripción de Loop 1"},
        {"id": 2, "title": "Loop 2", "description": "Descripción de Loop 2"},
    ]
    return JsonResponse(sample_data, safe=False)