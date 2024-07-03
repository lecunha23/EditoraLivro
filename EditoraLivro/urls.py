# EditoraLivro/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authors.urls')),
    path('books/', include('books.urls')),
]

# Adicione outras rotas aqui