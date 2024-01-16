from django.urls import path
from .views import escolher_fornecedor

urlpatterns = [
    path('escolher-fornecedor/', escolher_fornecedor, name='escolher_fornecedor'),
    # ... outras rotas do aplicativo ...
]
