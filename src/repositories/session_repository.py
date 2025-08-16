from src.entities.session import Session
from src.utils.jwt import JWT
from datetime import datetime, timedelta
from sqlalchemy.orm import Session as DBSession
from src.entities.user import User

class SessionRepository:  
    def __init__(self, db: DBSession): 
        self.db = db
        self.jwt = JWT()

    def create_session(self, user_id: int): 
        existing_session = self.active_sessions(user_id).first()
        
        if existing_session:
            return existing_session
        
        session = Session(user_id=user_id)
        session.access_token = self.jwt.encode({"user_id": user_id, "timestamp": datetime.now().timestamp()})
        session.expires_at = datetime.now() + timedelta(days=90)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def delete_session(self, user_id: int): 
        user = self.db.query(User).filter(User.id == user_id).first()
        if user: 
            session = self.active_sessions(user_id) 
            for s in session:
                s.active = False
                self.db.commit()
                self.db.refresh(s)
        return None
    
    def active_sessions(self, user_id: int):
        return self.db.query(Session).filter(
            Session.user_id == user_id,
            Session.expires_at > datetime.now(),
            Session.active == True
        ).order_by(Session.expires_at.desc())