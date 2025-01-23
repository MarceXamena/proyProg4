#from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
#from sqlalchemy.orm import Session
#from typing import List
#from ..database import get_db
#from ..schemas import Observacion, ObservacionCreate, Fotografia, FotografiaCreate
#from ..services.observation_service import ObservationService
#from ..services.user_service import UserService

#router = APIRouter()
#observation_service = ObservationService()
#user_service = UserService()

#@router.post("/", response_model=Observacion)
#async def create_observation(
#    observation: ObservacionCreate,
#    db: Session = Depends(get_db),
#    current_user = Depends(user_service.get_current_user)
#):
#    return observation_service.create_observation(db, observation, current_user.id)

#@router.get("/", response_model=List[Observacion])
#async def get_observations(
#    skip: int = 0,
#    limit: int = 100,
#    db: Session = Depends(get_db),
#    current_user = Depends(user_service.get_current_user)
#):
#    return observation_service.get_observations(db, current_user.id, skip, limit)

#@router.post("/{observation_id}/photos", response_model=Fotografia)
#async def upload_photo(
#    observation_id: int,
#    file: UploadFile = File(...),
#    db: Session = Depends(get_db),
#    current_user = Depends(user_service.get_current_user)
#):
#    return observation_service.add_photo(db, observation_id, file, current_user.id)

#@router.get("/{observation_id}", response_model=Observacion)
#async def get_observation(
#    observation_id: int,
#    db: Session = Depends(get_db),
#    current_user = Depends(user_service.get_current_user)
#):
#    return observation_service.get_observation(db, observation_id, current_user.id)

