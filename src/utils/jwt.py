import os
import jwt
import dotenv

dotenv.load_dotenv()

class JWT: 
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET_KEY")
        self.algorithm = os.getenv("JWT_ALGORITHM")

    def encode(self, payload: dict):
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def decode(self, token: str):
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])