

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),
    path('<int:pk>/', views.detalhe_fornecedor, name='detalhe_fornecedor'),
    path('adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('<int:pk>/editar/', views.editar_fornecedor, name='editar_fornecedor'),  # Nova URL para edição
    path('<int:pk>/deletar/', views.deletar_fornecedor, name='deletar_fornecedor'),  # Nova URL para deletar
    path('home/', views.index, name='index'),
]
