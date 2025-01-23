#from fastapi import HTTPException, status
#from sqlalchemy.orm import Session
#from datetime import datetime, timedelta
#from jose import JWTError, jwt
#from passlib.hash import bcrypt
#from typing import Optional
#from models import Usuario
#from backend.schemas import UsuarioCreate, UsuarioUpdate
#import os
from sqlalchemy.orm import Session 
from sqlalchemy import func
from passlib.context import CryptContext
from models import Usuario, SolicitudCambioNivel
from schemas import UsuarioCreate
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from database import get_db
from fastapi.security.utils import get_authorization_scheme_param

SECRET_KEY = "e0310e28dcbdbd3c070e36083c30d8f8d514d9f8292eecc5041eedd186901cb3here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Simula una lista de bloqueo en memoria (en producción usar una base de datos o Redis)
blacklisted_tokens = set()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Función para crear un token de acceso
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Función para agregar un token a la lista de bloqueo
def invalidate_token(token: str):
    blacklisted_tokens.add(token)

# Función para verificar si un token está en la lista de bloqueo
def is_token_blacklisted(token: str):
    return token in blacklisted_tokens

# Función para decodificar y validar un token
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if is_token_blacklisted(token):
            raise JWTError("Token has been invalidated")
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Token error: {str(e)}")

# Funciones de hash de contraseñas
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Función para crear un nuevo usuario
def create_user(db: Session, user: UsuarioCreate):
    hashed_password = get_password_hash(user.password)
    db_user = Usuario(
        nombre=user.nombre,
        email=user.email,
        password=hashed_password,
        nivel_id=1,  # Nivel inicial por defecto
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Función para autenticar a un usuario
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

def get_current_user(request: Request, db: Session = Depends(get_db)):
    # Extraer el token directamente del encabezado Authorization
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        raise HTTPException(status_code=401, detail="Authorization token is missing")

    # El encabezado debe estar en el formato "Bearer <token>"
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token scheme")

    # Obtener el token sin el "Bearer "
    token = auth_header[7:]

    print(f"Token recibido: {token}")

    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Payload decodificado: {payload}")
        email: str = payload.get("sub")
        print(f"Email extraído del token: {email}")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        if is_token_blacklisted(token):
            raise HTTPException(status_code=401, detail="Token has been invalidated")

        # Buscar al usuario en la base de datos
        user = db.query(Usuario).filter(Usuario.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    except JWTError as e:
        print(f"Error al decodificar el token: {e}")
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")

# Función para notificar a los validadores
def notificar_validadores(db: Session):
    validadores = db.query(Usuario).filter(Usuario.nivel_id == 2).all()
    for validador in validadores:
        print(f"Notificación: Nueva solicitud pendiente para el usuario con ID {validador.id}")

def crear_solicitud_cambio_nivel(db: Session, usuario_id: int):
    solicitud = SolicitudCambioNivel(usuario_id=usuario_id)
    db.add(solicitud)
    db.commit()
    db.refresh(solicitud)
    notificar_validadores(db)
    return solicitud

def obtener_solicitudes_pendientes(db: Session):
    return db.query(SolicitudCambioNivel).filter(SolicitudCambioNivel.estado == "Pendiente").all()

def gestionar_solicitud(db: Session, solicitud_id: int, validador_id: int, aceptar: bool):
    print(f"Aceptar recibido: {aceptar}")
    solicitud = db.query(SolicitudCambioNivel).filter(SolicitudCambioNivel.id == solicitud_id).first()
    if not solicitud or solicitud.estado != "Pendiente":
        raise HTTPException(status_code=404, detail="Solicitud no encontrada o ya gestionada")
    
    solicitud.estado = "Aceptada" if aceptar else "Rechazada"
    solicitud.validador_id = validador_id
    solicitud.fecha_resolucion = func.now()

    if aceptar:
        usuario = db.query(Usuario).filter(Usuario.id == solicitud.usuario_id).first()
        usuario.nivel_id = 2  # Cambia el nivel a "Validador"

    db.commit()
    return solicitud


