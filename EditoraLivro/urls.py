from django.contrib import admin
from django.urls import path, include
from . import views  # Importe sua view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a URL raiz
    path('author/', include('authors.urls')),
    path('books/', include('books.urls')),
    path('fornecedores/', include('fornecedores.urls')),

]
