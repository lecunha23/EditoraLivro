from django.contrib import admin
from django.urls import path, include
from . import views  # Importe sua view home
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a URL raiz
    path('author/', include('authors.urls')),
    path('books/', include('books.urls')),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('fornecedores/', include('fornecedores.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),


]
