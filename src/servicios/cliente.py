from bson import ObjectId

from db.mongo import get_collection
from modelos.cliente import Cliente

coleccionCliente = get_collection("clientes")

def obtenerClientes():
  items = []
  for item in coleccionCliente.find():
    items.append({
      "_id":item["_id"].__str__(),
      'identificacion': item["identificacion"],
      'nombre': item["nombre"],
      'apellido': item["apellido"],
      'email': item["email"],
      'celular': item["celular"]
    })
  return items

def crearCliente(item:Cliente):
  coleccionCliente.insert_one({
    'identificacion': item.identificacion,
    'nombre': item.nombre,
    'apellido': item.apellido,
    'email': item.email,
    'celular': item.celular
  })
  return item

def actualizarCliente(id:str, item:Cliente):
  coleccionCliente.update_one({"_id": ObjectId(id)},{
    '$set':{
      'identificacion': item.identificacion,
      'nombre': item.nombre,
      'apellido': item.apellido,
      'email': item.email,
      'celular': item.celular
    }
  })
  return item

def eliminarCliente(id:str):
  coleccionCliente.delete_one({"_id": ObjectId(id)})
  return id