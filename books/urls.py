from django.urls import path
from .views import livro_create

urlpatterns = [
    path('livro/new/', livro_create, name='livro_create'),
    # Adicione outras rotas aqui
]
