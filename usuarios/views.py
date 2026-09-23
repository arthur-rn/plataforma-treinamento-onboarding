from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from empresas.models import Empresa
from .forms import LoginEmpresaForm


def login_empresa_view(request, slug):
    # 1. Busca a empresa pelo slug da URL (ex: 'clinica-imagem')
    empresa = get_object_or_404(Empresa, slug=slug, ativo=True)

    # Se o usuário já estiver logado e for dessa empresa, vai direto para o dashboard
    if request.user.is_authenticated and request.user.empresa == empresa:
        return redirect('usuarios:dashboard', slug=empresa.slug)

    if request.method == 'POST':
        form = LoginEmpresaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # 2. Tenta autenticar o usuário
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # 3. REGRA DE SEGURANÇA MULTI-TENANT:
                # O colaborador só pode entrar se a empresa dele for a mesma da URL
                #Ou se ele for o Super Administrador geral
                if user.is_superuser or user.empresa == empresa:
                    login(request, user)
                    messages.success(request, f'Bem-vindo de volta, {user.first_name or user.username}!')
                    return redirect('usuarios:dashboard', slug=empresa.slug)
                else:
                    messages.error(request, 'Acesso negado: seu usuário não tem permissão de acesso nesta empresa.')
            else:
                messages.error(request, 'E-mail ou senha incorretos.')
    else:
        form = LoginEmpresaForm()

    context = {
        'empresa': empresa,
        'form': form,
    }
    return render(request, 'usuarios/login.html', context)


def logout_empresa_view(request, slug):
    empresa = get_object_or_404(Empresa, slug=slug)
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('usuarios:login', slug=empresa.slug)


@login_required
def dashboard_empresa_view(request, slug):
    empresa = get_object_or_404(Empresa, slug=slug, ativo=True)

    # Garante que um usuário logado não acesse o dashboard de outra empresa trocando a URL
    if not request.user.is_superuser and request.user.empresa != empresa:
        messages.error(request, 'Você não tem acesso a esta empresa.')
        return redirect('usuarios:login', slug=empresa.slug)

    context = {
        'empresa': empresa,
    }
    return render(request, 'usuarios/dashboard.html', context)