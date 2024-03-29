from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from ..repositories.classRepository import *

@csrf_exempt
def criar_sala_api(request):
    if request.method == 'POST':
        data = request.POST
        numero_sala = data.get('numero_sala')
        capacidade = data.get('capacidade')

        # Verifica se os campos obrigatórios foram fornecidos
        if not numero_sala or not capacidade:
            return HttpResponseBadRequest('Número da sala e capacidade são campos obrigatórios.')

        try:
            numero_sala = int(numero_sala)
            capacidade = int(capacidade)
        except ValueError:
            return HttpResponseBadRequest('Número da sala e capacidade devem ser números inteiros.')

        # Cria a sala utilizando a função do repository
        sala_id = criar_sala(numero_sala, capacidade)
        return JsonResponse({'sala_id': str(sala_id)})
    else:
        return HttpResponseBadRequest('Método não permitido.')

@csrf_exempt
def listar_salas_api(request):
    if request.method == 'GET':
        salas = listar_salas()
        for sala in salas:
            sala['_id'] = str(sala['_id'])  # Converte o ObjectId para string
        return JsonResponse(salas, safe=False)

@csrf_exempt
def detalhes_sala_api(request, sala_id):
    if request.method == 'GET':
        sala = obter_sala_por_id(sala_id)
        if sala:
            sala['_id'] = str(sala['_id'])
            return JsonResponse(sala)
        else:
            return HttpResponseBadRequest('Sala não encontrada.')

@csrf_exempt
def atualizar_sala_api(request, sala_id):
    if request.method == 'PUT':
        data = request.POST
        numero_sala = data.get('numero_sala')
        capacidade = data.get('capacidade')

        # Verifica se os campos obrigatórios foram fornecidos
        if not numero_sala or not capacidade:
            return HttpResponseBadRequest('Número da sala e capacidade são campos obrigatórios.')

        try:
            numero_sala = int(numero_sala)
            capacidade = int(capacidade)
        except ValueError:
            return HttpResponseBadRequest('Número da sala e capacidade devem ser números inteiros.')

        # Cria a sala utilizando a função do repository
        sala_id = atualizar_sala(sala_id, numero_sala, capacidade)
        return JsonResponse('Sala atualizada com sucesso')
    else:
        return HttpResponseBadRequest('Método não permitido.')

@csrf_exempt
def excluir_sala_api(request, sala_id):
    if request.method == 'DELETE':
        excluir_sala(sala_id)
        return JsonResponse({'message': 'Sala excluída com sucesso.'})
