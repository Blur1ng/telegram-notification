from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class VIPUser(Base):
    __tablename__ = "VIPUsers"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    notification = Column(Boolean, index=True)