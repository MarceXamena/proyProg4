from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, Session
from ..database import Base
from ..schemas import celestial_object_schema

class CelestialObject(Base):
    __tablename__ = "celestial_objects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    alternative_names = Column(String)
    object_type = Column(String, index=True)
    constellation = Column(String, index=True)
    best_visibility = Column(String)
    ra = Column(Float)  # Right Ascension
    dec = Column(Float)  # Declination
    magnitude = Column(Float)

    observations = relationship("Observation", back_populates="celestial_object")

def get_celestial_objects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CelestialObject).offset(skip).limit(limit).all()

def create_celestial_object(db: Session, celestial_object: celestial_object_schema.CelestialObjectCreate):
    db_celestial_object = CelestialObject(**celestial_object.dict())
    db.add(db_celestial_object)
    db.commit()
    db.refresh(db_celestial_object)
    return db_celestial_object

