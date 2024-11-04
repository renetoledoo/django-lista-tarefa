import json
from django.shortcuts import render, redirect
from tarefas.models import Tarefas
from django.http import JsonResponse

def renderizar(request):
    print('Método -> ', request.method)
    tarefasNovas = Tarefas.objects.filter(status='N')
    tarefasConcluidas = Tarefas.objects.filter(status='C')
    tarefasAndamento = Tarefas.objects.filter(status='A')

    retorno = {
        'tarefasNovas': tarefasNovas,
        'tarefasAndamento': tarefasAndamento,
        'tarefasConcluidas': tarefasConcluidas
    }

    contexto = {'tarefas': retorno}
    print(f'Tarefas novas: {tarefasNovas.count()}')

    if request.method == 'GET':
        return render(request, 'index.html', contexto)
    
    elif request.method == 'POST':
        print(request.POST)
        nomeTarefa = request.POST['nomeTarefa']
        area = request.POST['area']
        prioridade = request.POST['prioridade']
        
        print('Nome taredfa: ',nomeTarefa)
        
        prioridade_sigla = 'L' if prioridade == 'Leve' else ('M' if prioridade == 'Moderada' else 'A')

        tarefa = Tarefas(titulo=nomeTarefa, area=area, prioridade=prioridade_sigla, status='N')
        tarefa.save()

        tarefasNovas = Tarefas.objects.filter(status='N')
        tarefasConcluidas = Tarefas.objects.filter(status='C')
        tarefasAndamento = Tarefas.objects.filter(status='A')

        retorno = {
            'tarefasNovas': tarefasNovas,
            'tarefasAndamento': tarefasAndamento,
            'tarefasConcluidas': tarefasConcluidas
        }

        contexto = {'tarefas': retorno}
        return redirect('salvar')


def atualizarStatus(request, tarefa_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        novo_status = data.get('status')

        try:
            tarefa = Tarefas.objects.get(id=tarefa_id)
            tarefa.status = novo_status 
            tarefa.save()  
            
            return JsonResponse({'success': True, 'message': 'Status atualizado com sucesso!'})
        except Tarefas.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Tarefa não encontrada!'}, status=404)
    
    return JsonResponse({'success': False, 'message': 'Método não permitido!'}, status=405)

    