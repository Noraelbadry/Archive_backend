from sqlalchemy import Column, Integer, SmallInteger, String, Text, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class ArtifactPart(Base):
    __tablename__ = "artifact_parts"
    __table_args__ = {"schema": "public"}

    part_id         = Column(Integer, primary_key=True, autoincrement=True)
    artifact_id     = Column(Integer, nullable=False)
    part_name       = Column(String(150), nullable=False)
    description     = Column(Text, nullable=False)
    historical_note = Column(Text)
    sort_order      = Column(SmallInteger, default=0)
    is_active       = Column(Boolean, default=True)