"""BASE MODELS"""
import datetime

from sqlalchemy import Column, Integer, DateTime

from src.database import Base


class BaseModel(Base):
    """Abstract base model"""
    
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=False), default=datetime.datetime.now())