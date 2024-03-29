from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['base_de_dados']
salas_collection = db['salas']

def listar_salas():
    return list(salas_collection.find())

def obter_sala_por_id(sala_id):
    return salas_collection.find_one({'_id': ObjectId(sala_id)})

def criar_sala(numero_sala, capacidade):
    sala = {'numero_sala': numero_sala, 'capacidade': capacidade}
    result = salas_collection.insert_one(sala)
    return result.inserted_id

def atualizar_sala(sala_id, numero_sala, capacidade):
    salas_collection.update_one({'_id': ObjectId(sala_id)}, {'$set': {'numero_sala': numero_sala, 'capacidade': capacidade}})

def excluir_sala(sala_id):
    salas_collection.delete_one({'_id': ObjectId(sala_id)})
