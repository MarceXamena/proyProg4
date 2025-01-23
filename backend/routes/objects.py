#from fastapi import APIRouter, Depends, HTTPException, status
#from sqlalchemy.orm import Session
#from typing import List
#from ..database import get_db
#from ..schemas import ObjetoCeleste, ObjetoCelesteCreate, Favorito, FavoritoCreate
#from ..services.user_service import UserService
#from ..services.object_service import ObjectService

#router = APIRouter()
#object_service = ObjectService()
#user_service = UserService()

#@router.get("/", response_model=List[ObjetoCeleste])
#async def get_objects(
#    skip: int = 0,
#    limit: int = 100,
#    db: Session = Depends(get_db)
#):
#    return object_service.get_objects(db, skip, limit)

#@router.get("/{object_id}", response_model=ObjetoCeleste)
#async def get_object(object_id: int, db: Session = Depends(get_db)):
#    return object_service.get_object(db, object_id)

#@router.post("/favorites", response_model=Favorito)
#async def add_favorite(
#    favorite: FavoritoCreate,
#    db: Session = Depends(get_db),
#    current_user = Depends(user_service.get_current_user)
#):
#    return object_service.add_favorite(db, favorite, current_user.id)

#@router.get("/favorites", response_model=List[ObjetoCeleste])
#async def get_favorites(
#    db: Session = Depends(get_db),
#    current_user = Depends(user_service.get_current_user)
#):
#    return object_service.get_favorites(db, current_user.id)

