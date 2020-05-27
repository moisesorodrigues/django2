from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from django.contrib.auth.models import User

from django.contrib import auth, messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from aplicativoreceitas.models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(modo_edicao=False)

    paginator = Paginator(receitas, 5)

    page = request.GET.get('page')

    receitas_por_pagina = paginator.get_page(page)
    
    dados = {
        'receitas': receitas_por_pagina
    }
    
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_por_id = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', receita_por_id)

def adicionar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        imagem_receita = request.FILES['imagem_receita']
        
        usuario = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(usuario=usuario, 
                                            nome_receita=nome_receita, 
                                            ingredientes=ingredientes, 
                                            modo_preparo=modo_preparo, 
                                            tempo_preparo=tempo_preparo, 
                                            rendimento=rendimento, 
                                            categoria=categoria, 
                                            imagem_receita=imagem_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/adiciona_receita.html')

def excluir_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    dados = {
        'receita': receita
    }
    
    return render(request, 'receitas/edita_receita.html', dados)

def atualizar_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        receita_obtida = Receita.objects.get(pk=receita_id)
        receita_obtida.nome_receita = request.POST['nome_receita']
        receita_obtida.ingredientes = request.POST['ingredientes']
        receita_obtida.modo_preparo = request.POST['modo_preparo']
        receita_obtida.tempo_preparo = request.POST['tempo_preparo']
        receita_obtida.rendimento = request.POST['rendimento']
        receita_obtida.categoria = request.POST['categoria']
        
        if 'imagem_receita' in request.FILES:
            receita_obtida.imagem_receita = request.FILES['imagem_receita']
        
        receita_obtida.save()

        return redirect('dashboard')