
from bson.objectid import ObjectId
from models import UsuarioSchema, UpdateUsuarioModel
from database import usuarios_collection, usuario_helper

# Agregar un nuevo usuario
async def agregar_usuario(usuario_data: dict) -> dict:
    usuario = await usuarios_collection.insert_one(usuario_data)
    nuevo_usuario = await usuarios_collection.find_one({"_id": usuario.inserted_id})
    return usuario_helper(nuevo_usuario)

# Listar todos los usuarios
async def listar_usuarios():
    usuarios = []
    async for usuario in usuarios_collection.find():
        usuarios.append(usuario_helper(usuario))
    return usuarios

# Obtener un usuario por ID
async def obtener_usuario(id: str) -> dict:
    usuario = await usuarios_collection.find_one({"_id": ObjectId(id)})
    if usuario:
        return usuario_helper(usuario)

# Actualizar un usuario por ID
async def actualizar_usuario(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    usuario = await usuarios_collection.find_one({"_id": ObjectId(id)})
    if usuario:
        actualizado_usuario = await usuarios_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if actualizado_usuario:
            return True
        return False

# Eliminar un usuario por ID
async def eliminar_usuario(id: str):
    usuario = await usuarios_collection.find_one({"_id": ObjectId(id)})
    if usuario:
        await usuarios_collection.delete_one({"_id": ObjectId(id)})
        return True
