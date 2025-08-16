from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import ConfigDict

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str
    scope: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    id: int
    github_id: int
    github_username: str
    name: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    blog: Optional[str] = None
    github_url: Optional[str] = None
    html_url: Optional[str] = None
    public_repos: int = 0
    public_gists: int = 0
    followers: int = 0
    following: int = 0
    hireable: bool = False
    site_admin: bool = False
    user_type: str = "User"
    github_created_at: Optional[datetime] = None
    github_updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    is_active: bool = True
    is_verified: bool = False


class SessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) 

    id: int
    user_id: int
    access_token: str
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class AuthResponse(BaseModel):
    user: UserResponse
    session: SessionResponse
    message: str = "Authentication successful"


class LogoutRequest(BaseModel):
    user_id: int