from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session
from ..database import Base
from ..schemas import user_schema

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_validator = Column(Boolean, default=False)
    points = Column(Integer, default=0)

    observations = relationship("Observation", back_populates="observer")

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: user_schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_password(db: Session, user_id: int, new_hashed_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.hashed_password = new_hashed_password
        db.commit()
        return user
    return None

def update_user_validator_status(db: Session, user_id: int, is_validator: bool):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.is_validator = is_validator
        db.commit()
        return user
    return None

def increase_user_points(db: Session, user_id: int, points: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.points += points
        db.commit()
        return user
    return None

