from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Nivel(Base):
    __tablename__ = "niveles"
    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    puntos = Column(Integer, default=0)
    fecha_registro = Column(DateTime, default=func.now())
    nivel_id = Column(Integer, ForeignKey("niveles.id"), default=1)
    password = Column(String, nullable=False)

    nivel = relationship("Nivel")

class SolicitudCambioNivel(Base):
    __tablename__ = "solicitudes_cambio_nivel"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    estado = Column(String, default="Pendiente")
    fecha_solicitud = Column(DateTime, default=func.now())
    validador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    fecha_resolucion = Column(DateTime, nullable=True)

    usuario = relationship("Usuario", foreign_keys=[usuario_id])
    validador = relationship("Usuario", foreign_keys=[validador_id])