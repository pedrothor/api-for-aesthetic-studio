from django.shortcuts import render
from django.contrib import messages
from .forms import AgendamentoForm


def index(request):

    form = AgendamentoForm()
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            form = AgendamentoForm()
            messages.success(request, 'Agendamento concluído!')
        else:
            form = AgendamentoForm()
            messages.error(request, form.errors)

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)
