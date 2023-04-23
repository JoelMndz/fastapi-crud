from pydantic import BaseModel

class Cliente(BaseModel):
  identificacion:str
  nombre:str
  apellido:str
  email:str
  celular:str
