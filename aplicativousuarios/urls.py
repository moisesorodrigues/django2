from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('adicionar/receita', views.adicionar_receita, name='adicionar_receita'),
]