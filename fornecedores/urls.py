
from django.urls import path
from .views import cadastrar_fornecedor

urlpatterns = [
    path('fornecedores/cadastrar/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    # Outras URLs...
]
