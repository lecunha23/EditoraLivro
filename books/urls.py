from django.urls import path
from .views import livro_create, livro_list, livro_update, livro_delete
from . import views


urlpatterns = [
    path('livro/new/', livro_create, name='livro_create'),
    path('livros/', livro_list, name='livro_list'),
    path('livro/<int:pk>/', views.LivroDetailView.as_view(), name='livro_detail'),
    path('livro/<int:pk>/edit/', livro_update, name='livro_update'),
    path('livro/<int:pk>/delete/', livro_delete, name='livro_delete'),




    # Adicione outras rotas aqui
]
