from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey  
from src.database.core import base  
from datetime import datetime
from sqlalchemy.orm import relationship
from src.entities.base import TimestampMixin

class Session(base, TimestampMixin):
    __tablename__ = "sessions" 

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String, unique=True, index=True)
    expires_at = Column(DateTime)  
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False, index=True)
    user = relationship("User", back_populates="sessions")
    active = Column(Boolean, default=True)