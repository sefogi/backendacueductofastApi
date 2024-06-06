from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel

# Configuración de la base de datos
MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.acueducto

usuarios_collection = database.get_collection("usuarios")

# Función para convertir un documento de MongoDB a un diccionario de Python
def usuario_helper(usuario) -> dict:
    return {
        "id": str(usuario["_id"]),
        "contrato": usuario["contrato"],
        "nombre": usuario["nombre"],
        "apellidos": usuario["apellidos"],
        "lectura": usuario["lectura"],
        "direccion": usuario["direccion"],
    }
