from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from routes import users, observations, objects, rankings
from database import Base, engine

# Crear las tablas en la base de datos
#Base.metadata.create_all(bind=engine)


app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(users.router, prefix="/users", tags=["users"])
#app.include_router(observations.router, prefix="/api/observations", tags=["observations"])
#app.include_router(objects.router, prefix="/api/objects", tags=["objects"])
#app.include_router(rankings.router, prefix="/api/rankings", tags=["rankings"])

