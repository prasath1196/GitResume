import os
import dotenv
from fastapi import Request
import httpx
from src.auth.model import AccessTokenResponse
from src.entities.user  import User
import ipdb
from src.repositories.user_repository import UserRepository  
from src.repositories.session_repository import SessionRepository 
from src.database.core import get_db
from src.database.core import  DBSession
from src.auth.model import UserResponse, SessionResponse, AuthResponse
dotenv.load_dotenv()
class AuthService: 
    def __init__(self): 
        self.db = DBSession()
        self.client_id = os.getenv('GITHUB_CLIENT_ID')
        self.client_secret = os.getenv('GITHUB_CLIENT_SECRET')
        self.redirect_uri = os.getenv('GITHUB_CALLBACK_URL')
        self.access_token_url = os.getenv('GITHUB_ACCESS_TOKEN_URL')
        self.scope = "repo"
        self.user_repo = UserRepository(self.db)
        self.session_repo = SessionRepository(self.db)

    def login_url(self): 
        return f"https://github.com/login/oauth/authorize?client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope={self.scope}"

    def logout(self, user_id: int): 
        self.session_repo.delete_session(user_id)
        return {"message": "Logged out successfully"}
    
    async def callback(self, request: Request):  
        code = request.query_params.get("code")
        return await self._get_access_token(code)

    async def _get_access_token(self, code: str): 
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "redirect_uri": self.redirect_uri
        }
        async with httpx.AsyncClient() as client: 
            access_token_response = await client.post(self.access_token_url, data=data, headers={"Accept": "application/json"})
            access_token_data = AccessTokenResponse(**access_token_response.json())        
            user_response = await client.get(self._user_info_url(), 
                                             headers={"Authorization": f"Bearer {access_token_data.access_token}"})
            user_data = user_response.json() 
            user_data["access_token"] = access_token_data.access_token
            user = self.user_repo.upsert_user(user_data) 
            session = self.session_repo.create_session(user.id) 
            return AuthResponse(user=UserResponse.model_validate(user), 
                                session=SessionResponse.model_validate(session))
        
    def _user_info_url(self): 
        return f"https://api.github.com/user"
