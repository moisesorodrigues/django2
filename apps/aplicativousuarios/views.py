from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib import auth, messages

from aplicativoreceitas.models import Receita

def cadastrar(request):
    """ Realiza o cadastro de um novo usuário """
    if request.method == 'POST':
        nome = request.POST['nome']
        if validarAtributo(nome):
            messages.error(request, 'O nome deve ser informado!')
            return redirect('cadastrar')

        email = request.POST['email']
        if validarAtributo(email):
            messages.error(request, 'O email deve ser informado!')
            return redirect('cadastrar')

        password = request.POST['password']
        password2 = request.POST['password2']
        if validarIgualdadeSenhas(password, password2):
            messages.error(request, 'As senhas devem ser iguais!')
            return redirect('cadastrar')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já associado com um usuário cadastrado!')
            return redirect('cadastrar')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome já associado com um usuário cadastrado!')
            return redirect('cadastrar')
        
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login do usuário através do e-mail e password"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        if validarAtributo(email) or validarAtributo(password):
            messages.error(request, 'E-mail e/ou senha NÃO informado(s)!')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
        else:
            messages.error(request, 'Nome NÃO associado com o endereço de email informado!')
            return render(request, 'usuarios/login.html')
        user = auth.authenticate(request, username=nome, password=password)
        if user is not None:
            auth.login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(usuario=id)

        dados = {
        'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def validarAtributo(atributo):
    return not atributo.strip()

def validarIgualdadeSenhas(senha, confirmacaoSenha):
    return senha != confirmacaoSenha