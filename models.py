from django.db import models
from django.contrib.auth.models import User


class Podologia(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    preco = models.CharField(max_length=4, null=False, blank=False)

    class Meta:
        db_table = 'podologia'
        verbose_name = 'servico_podologia'
        verbose_name_plural = 'servicos_podologia'

    def __str__(self):
        return self.nome


class ManicurePedicure(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    preco = models.CharField(max_length=4, null=False, blank=False)

    class Meta:
        db_table = 'manicurePedicure'
        verbose_name = 'servico_manicurepedicure'
        verbose_name_plural = 'servicos_manicurepedicure'

    def __str__(self):
        return self.nome


class Depilacao(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    preco = models.CharField(max_length=4, null=False, blank=False)

    class Meta:
        db_table = 'depilacao'
        verbose_name = 'servico_depilacao'
        verbose_name_plural = 'servicos_depilacao'

    def __str__(self):
        return self.nome


class Cilios(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    preco = models.CharField(max_length=4, null=False, blank=False)

    class Meta:
        db_table = 'cilios'
        verbose_name = 'servico_cilios'
        verbose_name_plural = 'servicos_cilios'

    def __str__(self):
        return self.nome


class Funcionario(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'funcionarios'
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'.title()


class Servico(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'servicos'
        verbose_name = 'servico'
        verbose_name_plural = 'servicos'

    def __str__(self):
        return f'{self.nome}'.title()


class HorarioPadrao(models.Model):
    horario = models.CharField(max_length=30)

    class Meta:
        db_table = 'horarios_padrao'
        verbose_name = 'horario_padrao'
        verbose_name_plural = 'horarios_padrao'

    def __str__(self):
        return self.horario


class Agendamento(models.Model):
    required_css_class = 'required'  # mostra os campos obrigatórios

    cliente = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    data = models.DateField(null=False, blank=False)
    servico = models.ForeignKey(Servico, null=False, blank=False, on_delete=models.CASCADE)
    horario = models.CharField(max_length=10, null=False, blank=False)
    # imagem = models.FileField(upload_to='staticfiles/', null=True, blank=True)  # deixando off por enquanto
    descricao = models.TextField('Descrição', null=False, blank=False, max_length=150)
    data_marcacao = models.DateField('Marcado em', auto_now=True)  # registra a data em que o horário foi marcado.
    atualizado = models.DateTimeField('Atualizado em', auto_now=True)  # registra a data em que o objeto foi atualizado.

    class Meta:
        db_table = 'agendamentos'
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'

    def __str__(self):
        return f'{self.horario} - {self.servico} - {self.data} - {self.descricao} - {self.data_marcacao}'

