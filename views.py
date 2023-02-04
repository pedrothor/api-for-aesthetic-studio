from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash  # serve para nao te desconectar ao trocar a senha
from django.contrib.auth.forms import PasswordChangeForm
from .forms import AgendamentoForm, CreateUserForm
from .models import Agendamentos
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:

        form = AgendamentoForm(request.POST)
        if str(request.method) == 'POST':
            form.instance.cliente = request.user  # pegando a instância com 'form.instance'
            if form.is_valid():
                form.save()
                form = AgendamentoForm()
                messages.success(request, 'Agendamento concluído!')

            else:
                form = AgendamentoForm()
                messages.error(request, form.errors)
    else:
        form = AgendamentoForm()
        messages.error(request, 'Faça login para agendar horário!')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def lista_horarios(request):

    user = request.user
    horarios = Agendamentos.objects.filter(cliente=user).order_by('data', 'horario')

    context = {
        'horarios': horarios,
    }

    return render(request, 'lista_horarios.html', context)\



@login_required(login_url='login')
def editar_horario(request, pk):

    horario = Agendamentos.objects.get(id=pk)
    form = AgendamentoForm(instance=horario)
    if str(request.method) == 'POST':
        form = AgendamentoForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Horário editado com sucesso!')
            return redirect('lista_horarios')
    context = {
        'form': form
    }
    return render(request, 'editar_horario.html', context)


@login_required(login_url='login')
def deletar_horario(request, pk):

    horario = Agendamentos.objects.get(id=pk)

    if str(request.method) == 'POST':
        horario.delete()
        messages.error(request, 'Horário deletado com sucesso!', fail_silently=True)
        return redirect('lista_horarios')
    context = {
        'horario': horario
    }
    return render(request, 'deletar_horario.html', context)


@login_required(login_url='login')
def trocar_senha(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('index')
        else:
            form = PasswordChangeForm(user=request.user)
            messages.error(request, 'Erro ao alterar senha')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form
    }

    return render(request, 'change_password.html', context)


def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = str(form.cleaned_data.get('username')).title()
            messages.success(request, f"Usuário '{user}' criado com sucesso!")
            return redirect('login')
    context = {
        'form': form,
    }

    return render(request, 'register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Usuário ou senha incorreta.')

    context = {}

    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):

    logout(request)

    return redirect('index')

