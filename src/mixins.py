import datetime

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, DateTime, Boolean


class BaseModelMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id =  Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=False), default=datetime.datetime.now())
    is_deleted = Column(Boolean(), default=False)