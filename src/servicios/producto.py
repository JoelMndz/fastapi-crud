from bson import ObjectId

from db.mongo import get_collection
from modelos.producto import Producto

coleccionProductos = get_collection("productos")

def obtenerProductos():
  items = []
  for item in coleccionProductos.find():
    items.append({
      "_id":item["_id"].__str__(),
      'nombre': item["nombre"],
      'marca': item["marca"],
      'categoria': item["categoria"],
      'precio': item["precio"],
      'stock': item["stock"]
    })
  return items

def crearProducto(producto: Producto):
  coleccionProductos.insert_one({
    'nombre': producto.nombre,
    'marca': producto.marca,
    'categoria': producto.categoria,
    'precio': producto.precio,
    'stock': producto.stock
  })
  return producto

def actualizarProducto(id:str, producto:Producto):
  coleccionProductos.update_one({"_id": ObjectId(id)},{
    '$set':{
      'nombre': producto.nombre,
      'marca': producto.marca,
      'categoria': producto.categoria,
      'precio': producto.precio,
      'stock': producto.stock   
    }
  })
  return producto

def eliminarProducto(id:str):
  coleccionProductos.delete_one({"_id": ObjectId(id)})
  return id