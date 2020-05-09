from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(modo_edicao=False)

    dados = {
        'receitas': receitas
    }
    
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_por_id = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_por_id)

def pesquisar(request):
    receitas_pesquisadas = Receita.objects.order_by('-data_receita').filter(modo_edicao=False)

    if 'pesquisar' in request.GET:
        nome_receita_pesquisado = request.GET['pesquisar']

        if nome_receita_pesquisado:
            receitas_pesquisadas = receitas_pesquisadas.filter(nome_receita__icontains=nome_receita_pesquisado)
    
    dados = {
        'receitas': receitas_pesquisadas
    }
    
    return render(request, 'pesquisa.html', dados)