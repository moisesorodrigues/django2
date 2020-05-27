from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('pesquisar', pesquisar, name='pesquisar'),
    path('adicionar/receita', adicionar_receita, name='adicionar_receita'),
    path('excluir/<int:receita_id>', excluir_receita, name='excluir_receita'),
    path('editar/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualizar_receita', atualizar_receita, name='atualizar_receita'),
]