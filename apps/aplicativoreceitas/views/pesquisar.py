from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from aplicativoreceitas.models import Receita

def pesquisar(request):
    receitas_pesquisadas = Receita.objects.order_by('-data_receita').filter(modo_edicao=False)

    if 'pesquisar' in request.GET:
        nome_receita_pesquisado = request.GET['pesquisar']

        if nome_receita_pesquisado:
            receitas_pesquisadas = receitas_pesquisadas.filter(nome_receita__icontains=nome_receita_pesquisado)
    
    dados = {
        'receitas': receitas_pesquisadas
    }
    
    return render(request, 'receitas/pesquisa.html', dados)