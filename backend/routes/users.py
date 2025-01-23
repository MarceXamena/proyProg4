

#from fastapi import APIRouter, Depends, HTTPException
#from sqlalchemy.orm import Session
#from backend.schemas import UsuarioCreate, UsuarioOut
#from backend.models import Usuario
#from services.user_service import create_user
#from backend.database import SessionLocal
#from fastapi import APIRouter, Depends, HTTPException, Request
#from sqlalchemy.orm import Session
#from schemas import UsuarioCreate, UsuarioResponse, LoginData
#from services.user_service import create_user, authenticate_user, create_access_token
#from database import get_db
from models import Usuario
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from schemas import UsuarioCreate, UsuarioResponse, LoginData, GestionarSolicitud, UsuarioPerfil
from services.user_service import (
    create_user,
    authenticate_user,
    create_access_token,
    invalidate_token,
    decode_token,
    crear_solicitud_cambio_nivel,
    gestionar_solicitud,
    obtener_solicitudes_pendientes,
    get_current_user
    )
from database import get_db
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Ruta para registrar un usuario
@router.post("/register", response_model=UsuarioResponse)
def register_user(user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

# Ruta para iniciar sesión
@router.post("/login")
def login_user(login_data: LoginData, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# Ruta para cerrar sesión
@router.post("/logout")
def logout_user(request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token not provided or invalid format")
    token = token.split(" ")[1]
    invalidate_token(token)
    return {"message": "Logout successful"}

# Ruta protegida de ejemplo
@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    user_data = decode_token(token)
    return {"message": f"Welcome, {user_data['sub']}!"}

@router.post("/request-level-up")
def solicitar_cambio_nivel(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    if current_user.nivel_id != 1:
        raise HTTPException(status_code=403, detail="Solo usuarios principiantes pueden solicitar cambio de nivel")
    return crear_solicitud_cambio_nivel(db, current_user.id)

@router.get("/pending-requests")
def listar_solicitudes_pendientes(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    if current_user.nivel_id != 2:
        raise HTTPException(status_code=403, detail="Solo validadores pueden ver las solicitudes")
    return obtener_solicitudes_pendientes(db)

@router.post("/manage-request/{solicitud_id}")
def gestionar_cambio_nivel(
    solicitud_id: int,
    solicitud_data: GestionarSolicitud,  
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    if current_user.nivel_id != 2:
        raise HTTPException(status_code=403, detail="Solo validadores pueden gestionar solicitudes")
    return gestionar_solicitud(db, solicitud_id, current_user.id, solicitud_data.aceptar)

@router.get("/profile", response_model=UsuarioPerfil)
def get_user_profile(
    current_user: Usuario = Depends(get_current_user)
):
    return current_user