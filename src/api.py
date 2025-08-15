from src.commits.controller import router as commits_router
from src.auth.controller import router as auth_router

def register_routes(app):
    app.include_router(commits_router)
    app.include_router(auth_router)
