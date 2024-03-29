from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from ..repositories.reserveRepository import *

@csrf_exempt
def listar_reservas_sala_api(request, sala_id):
    if request.method == 'GET':
        reservas = listar_reservas_sala(sala_id)
        return JsonResponse(reservas, safe=False)

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
        data_hora_inicio = data.get('data_hora_inicio')  # Precisa ser convertido para datetime
        data_hora_fim = data.get('data_hora_fim')  # Precisa ser convertido para datetime
        materia = data.get('materia')
        professor = data.get('professor')
        reserva_id = criar_reserva(sala_id, data_hora_inicio, data_hora_fim, materia, professor)
        return JsonResponse({'reserva_id': str(reserva_id)})

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
