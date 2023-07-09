from sqlalchemy import Column, String, Boolean, Integer

from src.database import Base
from src.mixins import BaseModelMixin




class User(Base, BaseModelMixin):

    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)