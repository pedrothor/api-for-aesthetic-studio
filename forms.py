from .models import Agendamento
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
import datetime


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'input--style-5', 'style': 'width: 300px;'}),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'input--style-5', 'style': 'width: 300px;'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input--style-5', 'style': 'width: 300px;'}),
            'email': forms.EmailInput(attrs={'class': 'input--style-5', 'style': 'width: 300px;'}),
        }


class TrocaSenhaForm(PasswordChangeForm):

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class DateForm(forms.DateInput):
    required_css_class = 'required'  # mostra os campos obrigatórios
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        hoje = datetime.datetime.now()
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', datetime.date.today())  # restringindo agendamentos para datas passadas
        self.attrs.setdefault('max', datetime.date(hoje.year, int(hoje.month) + 6, hoje.day))  # limitando a agendamento somente para 6 meses a frente

    class Meta:
        fields = ['data']


class AgendamentoForm(forms.ModelForm):
    required_css_class = 'required'  # mostra os campos obrigatórios

    class Meta:
        model = Agendamento
        fields = ['data', 'servico', 'horario', 'descricao']
        widgets = {
            'data': DateForm(attrs={'class': 'form-control', 'style': 'placeholder: "DD/MM/AAAA";'}),
            'servico': forms.Select(attrs={'class': 'form-control', 'style': 'placeholder: "Serviço";'}),
            'horario': forms.Select(attrs={'class': 'form-control', 'style': 'placeholder: "Horário"; width: 250px;'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'id': 'form-descricao', 'placeholder': 'Ex: unha encravada, banho em gel...', 'style': 'height: 100px; width: 250px;'}),
        }


class EditaUsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
