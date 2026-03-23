from sqlalchemy import Column, Integer, SmallInteger, String, Text, Boolean
from app.database import Base

class Museum(Base):
    __tablename__ = "museums"
    __table_args__ = {"schema": "public"}

    museum_id    = Column(Integer, primary_key=True, autoincrement=True)
    name         = Column(String(255), nullable=False)
    city         = Column(String(100))
    country      = Column(String(100))
    founded_year = Column(SmallInteger)
    description  = Column(Text)
    website_url  = Column(String(300))
    email        = Column(String(150))
    is_active    = Column(Boolean, default=True)