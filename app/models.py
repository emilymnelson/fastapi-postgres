# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CME(Base):
    __tablename__ = "cme"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(String)
    specialty = Column(String)
    hospital = Column(String)
