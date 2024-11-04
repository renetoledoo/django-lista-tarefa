from django.urls import path

from tarefas import views

urlpatterns = [
    path('', views.renderizar, name='salvar'),
    path('atualizar-status/<str:tarefa_id>/', views.atualizarStatus, name='atualizar_status')
    
]