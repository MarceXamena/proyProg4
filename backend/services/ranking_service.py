from sqlalchemy.orm import Session
from ..models import Usuario
from typing import List

class RankingService:
    def get_top_observers(self, db: Session, limit: int = 10) -> List[Usuario]:
        return db.query(Usuario).order_by(Usuario.puntos.desc()).limit(limit).all()

    def get_top_validators(self, db: Session, limit: int = 10) -> List[Usuario]:
        return db.query(Usuario).filter(
            Usuario.nivel_id == 2  # Nivel validador
        ).order_by(Usuario.puntos.desc()).limit(limit).all()

