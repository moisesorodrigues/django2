from django.shortcuts import render

from aplicativoairlines.forms import PesquisaPassagensForms, PessoaForms

def index(request):
    form = PesquisaPassagensForms()
    pessoa_form = PessoaForms()
    contexto = {'form':form, 'pessoa_form':pessoa_form}
    return render(request, 'airlines/index.html', contexto)

def pesquisar(request):
    if request.method == 'POST':
        form = PesquisaPassagensForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form':form, 'pessoa_form':pessoa_form}
            return render(request, 'airlines/pesquisa.html', contexto)
        else:
            contexto = {'form':form, 'pessoa_form':pessoa_form}
            return render(request, 'airlines/index.html', contexto)