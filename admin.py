from django.contrib import admin
from core.models import Agendamentos, HorariosPadrao, Servicos


@admin.register(Agendamentos)
class AgendamentosAdmin(admin.ModelAdmin):
    list_display = ('data', 'servico', 'horario', 'descricao', 'data_marcacao', 'atualizado',)


@admin.register(HorariosPadrao)
class HorariosPadraoAdmin(admin.ModelAdmin):
    list_display = ('horario',)


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
