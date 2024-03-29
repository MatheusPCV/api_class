from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['base_de_dados']
reservas_collection = db['reservas']

def listar_reservas_sala(sala_id):
    return list(reservas_collection.find({'sala_id': sala_id}))

def obter_reserva_por_id(reserva_id):
    return reservas_collection.find_one({'_id': ObjectId(reserva_id)})

def criar_reserva(sala_id, data_hora_inicio, data_hora_fim, materia, professor):
    reserva = {'sala_id': sala_id, 'data_hora_inicio': data_hora_inicio, 'data_hora_fim': data_hora_fim,
               'materia': materia, 'professor': professor}
    result = reservas_collection.insert_one(reserva)
    return result.inserted_id

def atualizar_reserva(reserva_id, data_hora_inicio, data_hora_fim, materia, professor):
    reservas_collection.update_one({'_id': ObjectId(reserva_id)}, {'$set': {'data_hora_inicio': data_hora_inicio,
                                                                             'data_hora_fim': data_hora_fim,
                                                                             'materia': materia,
                                                                             'professor': professor}})

def excluir_reserva(reserva_id):
    reservas_collection.delete_one({'_id': ObjectId(reserva_id)})
