import os
import dotenv
from fastapi import Request
import httpx
from src.auth.model import AccessTokenResponse

dotenv.load_dotenv()


class AuthService: 
    def __init__(self): 
        self.client_id = os.getenv('GITHUB_CLIENT_ID')
        self.client_secret = os.getenv('GITHUB_CLIENT_SECRET')
        self.redirect_uri = os.getenv('GITHUB_CALLBACK_URL')
        self.access_token_url = os.getenv('GITHUB_ACCESS_TOKEN_URL')
        self.scope = "repo"

    def login_url(self): 
        return f"https://github.com/login/oauth/authorize?client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope={self.scope}"

    def logout(self): 
        pass 
        
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
            response = await client.post(self.access_token_url, data=data, headers={"Accept": "application/json"})
            response_data = AccessTokenResponse(**response.json())
            
            user_response = await client.get(self._user_info_url(), 
                                             headers={"Authorization": f"Bearer {response_data.access_token}"})
        return user_response.json()

    def _user_info_url(self): 
        return f"https://api.github.com/user"
