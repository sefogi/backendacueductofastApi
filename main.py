from fastapi import FastAPI, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from models import UsuarioSchema, UpdateUsuarioModel
from crud import (
    agregar_usuario,
    listar_usuarios,
    obtener_usuario,
    actualizar_usuario,
    eliminar_usuario,
)

app = FastAPI()

@app.post("/usuarios/", response_description="Agregar nuevo usuario", response_model=UsuarioSchema)
async def crear_usuario(usuario: UsuarioSchema = Body(...)):
    usuario = jsonable_encoder(usuario)
    nuevo_usuario = await agregar_usuario(usuario)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=nuevo_usuario)

@app.get("/usuarios/", response_description="Listar todos los usuarios", response_model=List[UsuarioSchema])
async def obtener_usuarios():
    usuarios = await listar_usuarios()
    return usuarios

@app.get("/usuarios/{id}", response_description="Obtener un usuario por ID", response_model=UsuarioSchema)
async def obtener_usuario_por_id(id: str):
    usuario = await obtener_usuario(id)
    if usuario is None:
        raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")
    return usuario

@app.put("/usuarios/{id}", response_description="Actualizar un usuario", response_model=UsuarioSchema)
async def actualizar_usuario_por_id(id: str, usuario: UpdateUsuarioModel = Body(...)):
    usuario = {k: v for k, v in usuario.dict().items() if v is not None}
    actualizado = await actualizar_usuario(id, usuario)
    if actualizado:
        usuario_actualizado = await obtener_usuario(id)
        return usuario_actualizado
    raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")

@app.delete("/usuarios/{id}", response_description="Eliminar un usuario")
async def eliminar_usuario_por_id(id: str):
    eliminado = await eliminar_usuario(id)
    if eliminado:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")
