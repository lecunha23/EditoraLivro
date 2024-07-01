from django.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authors.urls')),  # Inclui as URLs do aplicativo authors
    # outras URLs do projeto, se houver
]
