from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),  # Lista de autores
    path('author/<int:pk>/', views.author_detail, name='author_detail'),  # Detalhes do autor
    path('author/new/', views.author_create, name='author_create'),  # Formulário de criação de autor
    path('author/<int:pk>/edit/', views.author_update, name='author_update'),  # Formulário de edição de autor
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),  # Excluir autor (opcional)
]
