
from django.urls import path
from .views import cadastrar_fornecedor, lista_fornecedores, detalhe_fornecedor

urlpatterns = [
    path('cadastrar/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('', lista_fornecedores, name='lista_fornecedores'),
    path('<int:pk>/', detalhe_fornecedor, name='detalhe_fornecedor'),
]
