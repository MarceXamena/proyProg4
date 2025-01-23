#from pydantic import BaseModel, EmailStr
#from datetime import datetime, time
#from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    puntos: int
    fecha_registro: datetime
    nivel_id: int

    class Config:
        orm_mode = True

class LoginData(BaseModel):
    email: EmailStr
    password: str

class GestionarSolicitud(BaseModel):
    aceptar: bool

class UsuarioPerfil(BaseModel):
    id: int
    nombre: str
    email: str
    nivel_id: int
    puntos: int

    class Config:
        orm_mode = True