from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, Session
from ..database import Base
from ..schemas import observation_schema

class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, index=True)
    location = Column(String)
    sky_conditions = Column(String)
    equipment = Column(String)
    description = Column(String)
    is_validated = Column(Boolean, default=False)

    observer_id = Column(Integer, ForeignKey("users.id"))
    celestial_object_id = Column(Integer, ForeignKey("celestial_objects.id"))

    observer = relationship("User", back_populates="observations")
    celestial_object = relationship("CelestialObject", back_populates="observations")
    photos = relationship("Photo", back_populates="observation")

class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    exposure_time = Column(Float)
    iso = Column(Integer)
    processing = Column(String)
    is_validated = Column(Boolean, default=False)

    observation_id = Column(Integer, ForeignKey("observations.id"))
    observation = relationship("Observation", back_populates="photos")

def create_observation(db: Session, observation: observation_schema.ObservationCreate):
    db_observation = Observation(**observation.dict(exclude={"photos"}))
    db.add(db_observation)
    db.commit()
    db.refresh(db_observation)

    for photo in observation.photos:
        db_photo = Photo(**photo.dict(), observation_id=db_observation.id)
        db.add(db_photo)
    
    db.commit()
    db.refresh(db_observation)
    return db_observation

