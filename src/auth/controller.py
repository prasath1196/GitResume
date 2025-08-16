from fastapi import APIRouter, Request
from src.auth.service import AuthService
import ipdb

router = APIRouter(
    prefix="/github/auth",
)

@router.get("/login")
def sign_in(): 
    return AuthService().login_url()

@router.delete("/logout/{user_id}")
def sign_out(user_id: int):
    return AuthService().logout(user_id)

@router.get("/callback")
async def callback(request: Request): 
    return await AuthService().callback(request)