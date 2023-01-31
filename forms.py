from .models import Agendamentos
from django import forms


class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = Agendamentos
        fields = ['data', 'servico', 'horario', 'descricao']
        widgets = {
            'data': forms.Select(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control', 'placeholder': '- Selecione -'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
