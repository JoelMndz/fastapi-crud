from fastapi import APIRouter
from servicios import cliente as clienteService
from modelos.cliente import Cliente

router = APIRouter()

@router.get('/cliente')
async def obtenerClientes():
  try:
    data = clienteService.obtenerClientes()
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}
  
@router.post('/cliente')
async def crearCliente(cliente: Cliente):
  try:
    data = clienteService.crearCliente(cliente)
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}
  
@router.patch('/cliente/{id}')
async def actualizarCliente(id:str, cliente: Cliente):
  try:
    data = clienteService.actualizarCliente(id, cliente)
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}
  
@router.delete('/cliente/{id}')
async def eliminarCliente(id:str):
  try:
    data = clienteService.eliminarCliente(id)
    return {'data': data}
  except Exception as error:
    return {'error': error.__str__()}