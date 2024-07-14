from django.urls import path
from . import views

urlpatterns = [
    path('pecas/', views.listar_pecas, name='listar_pecas'),
    path('pecas/criar/', views.criar_peca, name='criar_peca'),
    path('pecas/editar/<int:pk>/', views.editar_peca, name='editar_peca'),
    path('deletar/<int:pk>/', views.deletar_peca, name='deletar_peca'),

]


