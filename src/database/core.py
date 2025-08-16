from typing import Annotated 
from fastapi import Depends 
from sqlalchemy import create_engine, text, NullPool
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os 
import dotenv 

dotenv.load_dotenv() 

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, poolclass= NullPool, pool_pre_ping=True) 

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base() 

def get_db():  
    db = Session()
    try: 
        yield db
    finally: 
        db.close()

DBSession = Annotated[Session, Depends(get_db)]


