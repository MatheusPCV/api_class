from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from ..repositories.classRepository import *

@csrf_exempt
def listar_salas_api(request):
    if request.method == 'GET':
        salas = listar_salas()
        return JsonResponse(salas, safe=False)
    elif request.method == 'POST':
        data = request.POST
        numero_sala = int(data.get('numero_sala'))
        capacidade = int(data.get('capacidade'))
        sala_id = criar_sala(numero_sala, capacidade)
        return JsonResponse({'sala_id': str(sala_id)})

@csrf_exempt
def detalhes_sala_api(request, sala_id):
    if request.method == 'GET':
        sala = obter_sala_por_id(sala_id)
        if sala:
            return JsonResponse(sala)
        else:
            return HttpResponseBadRequest('Sala não encontrada.')

@csrf_exempt
def atualizar_sala_api(request, sala_id):
    if request.method == 'PUT':
        data = request.POST
        numero_sala = int(data.get('numero_sala'))
        capacidade = int(data.get('capacidade'))
        atualizar_sala(sala_id, numero_sala, capacidade)
        return JsonResponse({'message': 'Sala atualizada com sucesso.'})

@csrf_exempt
def excluir_sala_api(request, sala_id):
    if request.method == 'DELETE':
        excluir_sala(sala_id)
        return JsonResponse({'message': 'Sala excluída com sucesso.'})
