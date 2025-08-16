from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from src.database.core import base  
from datetime import datetime
from sqlalchemy.orm import relationship
from src.entities.base import TimestampMixin

class User(base, TimestampMixin):  # Fixed: base.Model → base
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    # GitHub-specific fields
    github_id = Column(Integer, unique=True, nullable=False, index=True)
    github_username = Column(String(255), unique=True, nullable=False, index=True)
    node_id = Column(String(255), nullable=True)
    
    # Profile information
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    avatar_url = Column(Text, nullable=True)
    bio = Column(Text, nullable=True)
    location = Column(String(255), nullable=True)
    company = Column(String(255), nullable=True)
    blog = Column(Text, nullable=True)
    website = Column(String(255), nullable=True)
    twitter_username = Column(String(255), nullable=True)
    
    # GitHub URLs
    github_url = Column(String(255), nullable=True)
    html_url = Column(Text, nullable=True)
    
    # GitHub stats
    public_repos = Column(Integer, default=0)
    public_gists = Column(Integer, default=0)
    followers = Column(Integer, default=0)
    following = Column(Integer, default=0)
    
    # GitHub metadata
    hireable = Column(Boolean, default=False)
    site_admin = Column(Boolean, default=False)
    user_type = Column(String(50), default="User")
    
    # Timestamps
    github_created_at = Column(DateTime, nullable=True)  # When GitHub account was created
    github_updated_at = Column(DateTime, nullable=True)  # When GitHub profile was last updated
    last_login = Column(DateTime, nullable=True)

    # Status fields
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    is_blocked = Column(Boolean, default=False)
    is_suspended = Column(Boolean, default=False)
    is_locked = Column(Boolean, default=False)
    access_token = Column(String(255), nullable=True)
    sessions = relationship("Session", 
                            back_populates="user", 
                            uselist=True, 
                            lazy="select")