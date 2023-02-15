from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash  # serve para nao te desconectar ao trocar a senha
from django.contrib.auth.forms import PasswordChangeForm
from .forms import AgendamentoForm, CreateUserForm, EditaUsuarioForm
from .models import Agendamentos, HorariosPadrao, Servicos
from django.contrib.auth.decorators import login_required


def index(request):

    if request.user.is_authenticated:

        if request.method == 'GET':

            data = request.GET.get('data')
            request.session['data'] = data  # empacotando na session

            servico = request.GET.get('servico')
            request.session['servico'] = servico  # empacotando na session

            agendamentos = Agendamentos.objects.filter(data=data, servico=servico)
            horarios_ocupados = [agendamento.horario for agendamento in agendamentos]
            horarios_filtrados = HorariosPadrao.objects.all().exclude(horario__in=horarios_ocupados)

            request.session['horarios_filtrados'] = [h.horario for h in horarios_filtrados]  # assim pois o session nao armazena queryset

        form = AgendamentoForm(request.GET)

        if request.method == 'POST':
            form = AgendamentoForm(request.POST)
            horario_escolhido = HorariosPadrao.objects.filter(horario=request.POST.get('horario'))

            if form.is_valid():
                form.instance.cliente = request.user
                form.data = form.cleaned_data.get('data')
                form.servico = form.cleaned_data.get('servico')
                form.horario = horario_escolhido
                form.descricao = form.cleaned_data.get('descricao')
                form.save()
                messages.success(request, 'Agendamento concluído!')
                return redirect('index')
            else:
                form = AgendamentoForm()
                messages.error(request, 'Formulário inválido, por favor verifique as informações preenchidas')
    else:
        form = AgendamentoForm()
        messages.error(request, 'Faça login para agendar horário!')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def perfil_usuario(request):

    if request.method == 'POST':

        form = EditaUsuarioForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadas com sucesso!')
            print('SUCESSO!')
            return redirect(to='perfil_usuario')
        else:
            messages.error(request, 'Erro ao atualizar informações')
    else:
        form = EditaUsuarioForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'perfil_usuario.html', context)


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
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'login.html')


@login_required(login_url='login')
def logoutUser(request):

    logout(request)

    return redirect('index')
