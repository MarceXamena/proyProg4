#from fastapi import APIRouter, Depends
#from sqlalchemy.orm import Session
#from typing import List
#from ..database import get_db
#from ..schemas import Usuario
#from ..services.ranking_service import RankingService

#router = APIRouter()
#ranking_service = RankingService()

#@router.get("/top-observers", response_model=List[Usuario])
#async def get_top_observers(
#    limit: int = 10,
#    db: Session = Depends(get_db)
#):
#    return ranking_service.get_top_observers(db, limit)

#@router.get("/top-validators", response_model=List[Usuario])
#async def get_top_validators(
#    limit: int = 10,
#    db: Session = Depends(get_db)
#):
#    return ranking_service.get_top_validators(db, limit)

