from fastapi import APIRouter
from servicios import producto as productoService
from modelos.producto import Producto

router = APIRouter()

@router.get('/producto')
async def obtenerProductos():
  try:
    data = productoService.obtenerProductos()
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}
  
@router.post('/producto')
async def crearProducto(producto: Producto):
  try:
    data = productoService.crearProducto(producto)
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}
  
@router.patch('/producto/{id}')
async def actualizarProducto(id:str, producto: Producto):
  try:
    data = productoService.actualizarProducto(id, producto)
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}
  
@router.delete('/producto/{id}')
async def eliminarProducto(id:str):
  try:
    data = productoService.eliminarProducto(id)
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}