from .models import Agendamentos
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DateForm(forms.DateInput):
    required_css_class = 'required'  # mostra os campos obrigatórios
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        hoje = datetime.datetime.now()
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', datetime.date.today())  # restringindo agendamentos para datas passadas
        self.attrs.setdefault('max', datetime.date(hoje.year, hoje.month+10, hoje.day))  # limitando a agendamento somente para 1 ano a frente

    class Meta:
        fields = ['data']


class AgendamentoForm(forms.ModelForm):
    required_css_class = 'required'  # mostra os campos obrigatórios

    class Meta:
        model = Agendamentos
        fields = ['data', 'servico', 'horario', 'descricao']
        widgets = {
            'data': DateForm(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
