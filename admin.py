from django.contrib import admin
from core.models import Agendamento, HorarioPadrao, Servico, Podologia, ManicurePedicure, Depilacao, Cilios


@admin.register(Agendamento)
class AgendamentosAdmin(admin.ModelAdmin):
    list_display = ('data', 'servico', 'horario', 'descricao', 'data_marcacao', 'atualizado',)


@admin.register(HorarioPadrao)
class HorariosPadraoAdmin(admin.ModelAdmin):
    list_display = ('horario',)


@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Podologia)
class PodologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


@admin.register(ManicurePedicure)
class ManicurePedicureAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


@admin.register(Depilacao)
class DepilacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


@admin.register(Cilios)
class CiliosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
