from fastapi import FastAPI
from rutas import producto, cliente

app = FastAPI()

app.include_router(producto.router)
app.include_router(cliente.router)

@app.get("/")
async def root():
  return {"nombre": "API para la gestion de productos"}

