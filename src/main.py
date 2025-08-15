from fastapi import FastAPI
import uvicorn
from src.api import register_routes

app = FastAPI()

register_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)