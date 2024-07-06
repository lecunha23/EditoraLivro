

from django.urls import path
from .views import adicionar_fornecedor, lista_fornecedores, detalhe_fornecedor

urlpatterns = [
    path('', lista_fornecedores, name='lista_fornecedores'),
    path('<int:pk>/', detalhe_fornecedor, name='detalhe_fornecedor'),
    path('adicionar/', adicionar_fornecedor, name='adicionar_fornecedor'),
]
