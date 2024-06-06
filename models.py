
from pydantic import BaseModel, Field
from typing import Optional

class UsuarioSchema(BaseModel):
    contrato: str = Field(...)
    nombre: str = Field(...)
    apellidos: str = Field(...)
    lectura: float = Field(...)
    direccion: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "contrato": "12345",
                "nombre": "Juan",
                "apellidos": "Pérez",
                "lectura": 10.0,
                "direccion": "Calle Falsa 123"
            }
        }

class UpdateUsuarioModel(BaseModel):
    contrato: Optional[str]
    nombre: Optional[str]
    apellidos: Optional[str]
    lectura: Optional[int]
    direccion: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "contrato": "12345",
                "nombre": "Juan",
                "apellidos": "Pérez",
                "lectura": 150,
                "direccion": "Calle Falsa 123"
            }
        }
