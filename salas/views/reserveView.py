from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from ..repositories.reserveRepository import *
from datetime import datetime
from bson import json_util

@csrf_exempt
def listar_reservas_sala_api(request, sala_id):
    if request.method == 'GET':
        reservas = listar_reservas_sala(sala_id)

        # Converter ObjectId para string antes de retornar a resposta JSON
        reservas_json = json_util.dumps(reservas)

        return JsonResponse(reservas_json, safe=False)
    else:
        return HttpResponseBadRequest('Método não permitido.')


@csrf_exempt
def detalhes_reserva_api(request, sala_id, reserva_id):
    if request.method == 'GET':
        reserva = obter_reserva_por_id(reserva_id)
        if reserva and reserva['sala_id'] == sala_id:
            return JsonResponse(reserva)
        else:
            return HttpResponseBadRequest('Reserva não encontrada.')

@csrf_exempt
def criar_reserva_api(request, sala_id):
    if request.method == 'POST':
        data = request.POST
        data_inicio = data.get('data_inicio')
        hora_inicio = data.get('hora_inicio')
        data_fim = data.get('data_fim')
        hora_fim = data.get('hora_fim')
        nome_materia = data.get('nome_materia')
        nome_professor = data.get('nome_professor')

        # Verifica se os campos obrigatórios foram fornecidos
        if not data_inicio or not hora_inicio or not data_fim or not hora_fim or not nome_materia or not nome_professor:
            return HttpResponseBadRequest('Todos os campos são obrigatórios.')

        # Chama a função do repository para criar a reserva
        reserva_id = criar_reserva(sala_id, data_inicio, hora_inicio, data_fim, hora_fim, nome_materia, nome_professor)
        return JsonResponse({'reserva_id': str(reserva_id)})
    else:
        return HttpResponseBadRequest('Método não permitido.')

@csrf_exempt
def atualizar_reserva_api(request, sala_id, reserva_id):
    if request.method == 'PUT':
        data = request.POST
        data_hora_inicio = data.get('data_hora_inicio')  # Precisa ser convertido para datetime
        data_hora_fim = data.get('data_hora_fim')  # Precisa ser convertido para datetime
        materia = data.get('materia')
        professor = data.get('professor')
        atualizar_reserva(reserva_id, data_hora_inicio, data_hora_fim, materia, professor)
        return JsonResponse({'message': 'Reserva atualizada com sucesso.'})

@csrf_exempt
def excluir_reserva_api(request, sala_id, reserva_id):
    if request.method == 'DELETE':
        excluir_reserva(reserva_id)
        return JsonResponse({'message': 'Reserva excluída com sucesso.'})
