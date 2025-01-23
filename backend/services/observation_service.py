from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from ..models import Observacion, Fotografia
from ..schemas import ObservacionCreate, FotografiaCreate
import os
from datetime import datetime

class ObservationService:
    async def create_observation(self, db: Session, observation: ObservacionCreate, user_id: int):
        db_observation = Observacion(
            **observation.dict(),
            usuario_id=user_id,
            estado="pendiente"
        )
        db.add(db_observation)
        db.commit()
        db.refresh(db_observation)
        return db_observation

    def get_observations(self, db: Session, user_id: int, skip: int = 0, limit: int = 100):
        return db.query(Observacion).filter(
            Observacion.usuario_id == user_id
        ).offset(skip).limit(limit).all()

    def get_observation(self, db: Session, observation_id: int, user_id: int):
        observation = db.query(Observacion).filter(
            Observacion.id == observation_id,
            Observacion.usuario_id == user_id
        ).first()
        if not observation:
            raise HTTPException(status_code=404, detail="Observation not found")
        return observation

    async def add_photo(self, db: Session, observation_id: int, file: UploadFile, user_id: int):
        observation = self.get_observation(db, observation_id, user_id)
        
        # Guardar archivo
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
        
        # Crear registro de fotografía
        db_photo = Fotografia(
            observacion_id=observation_id,
            ruta_archivo=file_location,
            estado="pendiente"
        )
        db.add(db_photo)
        db.commit()
        db.refresh(db_photo)
        return db_photo

