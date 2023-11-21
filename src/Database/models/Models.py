from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..Database import Base

class example(Base):
    __tablename__ = "exampleModel"

    uID = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)