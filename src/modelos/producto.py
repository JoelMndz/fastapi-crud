from pydantic import BaseModel

class Producto(BaseModel):
  nombre:str
  marca:str
  categoria:str
  precio:float
  stock:int


