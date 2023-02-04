from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
                    index,
                    registerPage,
                    loginPage, logoutUser,
                    lista_horarios, editar_horario,
                    deletar_horario, trocar_senha,
                    )


urlpatterns = [
    path('', index, name='index'),
    path('lista_horarios/', lista_horarios, name='lista_horarios'),
    path('editar_horario/<str:pk>/', editar_horario, name='editar_horario'),
    path('deletar_horario/<str:pk>/', deletar_horario, name='deletar_horario'),
    path('trocar_senha/', trocar_senha, name='trocar_senha'),
    #  os paths para resetar senha precisam estar nomeados como estão abaixo
    path('resetar_senha/', auth_views.PasswordResetView.as_view(template_name='resetar_senha.html'), name='reset_password'),  # selecionar o email a enviar
    path('resetar_senha_email_enviado/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # envia o email para resetar a senha
    path('resetar_senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # relaciona o formulário para resetar senha com o link enviado
    path('resetar_senha_finalizado/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # mensagem de senha resetada com sucesso
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
]
