from django.urls import path
from .views import index, registerPage, loginPage, logoutUser, lista_horarios, editar_horario, deletar_horario


urlpatterns = [
    path('', index, name='index'),
    path('lista_horarios/', lista_horarios, name='lista_horarios'),
    path('editar_horario/<str:pk>/', editar_horario, name='editar_horario'),
    path('deletar_horario/<str:pk>/', deletar_horario, name='deletar_horario'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
]
