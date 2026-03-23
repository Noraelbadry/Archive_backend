from sqlalchemy import Column, Integer, String, Text, SmallInteger, Enum, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Artifact(Base):
    __tablename__ = "artifacts"
    __table_args__ = {"schema": "public"}
    artifact_id    = Column(Integer, primary_key=True, autoincrement=True)
    museum_id      = Column(Integer, nullable=True)
    name           = Column(String(255), nullable=False)
    origin         = Column(String(255))
    period         = Column(String(100))
    estimated_year = Column(SmallInteger)
    material       = Column(String(150))
    description    = Column(Text)
    image_path = Column(Text)
    model_path = Column(Text)
    audio_path = Column(Text)
    is_active      = Column(Integer, default=1)