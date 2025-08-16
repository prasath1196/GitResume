from src.entities.user import User
from sqlalchemy.orm import Session as DBSession
from typing import Optional
from datetime import datetime

class UserRepository: 
    def __init__(self, db: DBSession):
        self.db = db

    def upsert_user(self, user_data: dict) -> User:
        """Create or update user based on GitHub ID"""
        
        # Check if user already exists
        existing_user = self.db.query(User).filter(User.github_id == user_data["id"]).first()
        
        if existing_user:
            # Update existing user
            return self._update_existing_user(existing_user, user_data)
        else:
            # Create new user
            return self._create_new_user(user_data)
    
    def _create_new_user(self, user_data: dict) -> User:
        """Create a new user"""
        user = self._map_github_data_to_user(user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def _update_existing_user(self, existing_user: User, user_data: dict) -> User:
        """Update existing user with new data"""
        # Update fields
        existing_user.github_username = user_data["login"]
        existing_user.name = user_data.get("name")
        existing_user.email = user_data.get("email")
        existing_user.avatar_url = user_data.get("avatar_url")
        existing_user.bio = user_data.get("bio")
        existing_user.location = user_data.get("location")
        existing_user.company = user_data.get("company")
        existing_user.blog = user_data.get("blog")
        existing_user.github_url = user_data.get("html_url")
        existing_user.html_url = user_data.get("html_url")
        existing_user.public_repos = user_data.get("public_repos", 0)
        existing_user.public_gists = user_data.get("public_gists", 0)
        existing_user.followers = user_data.get("followers", 0)
        existing_user.following = user_data.get("following", 0)
        existing_user.hireable = user_data.get("hireable", False)
        existing_user.site_admin = user_data.get("site_admin", False)
        existing_user.user_type = user_data.get("type", "User")
        existing_user.github_updated_at = user_data.get("updated_at")
        existing_user.access_token = user_data.get("access_token")
        existing_user.last_login = datetime.now()
        existing_user.updated_at = datetime.now()
        
        # Save changes
        self.db.commit()
        self.db.refresh(existing_user)
        return existing_user
    
    def _map_github_data_to_user(self, user_data: dict) -> User:
        """Map GitHub data to User entity"""
        return User(
            github_id=user_data["id"],
            github_username=user_data["login"],
            name=user_data.get("name"),
            email=user_data.get("email"),
            avatar_url=user_data.get("avatar_url"),
            bio=user_data.get("bio"),
            location=user_data.get("location"),
            company=user_data.get("company"),
            blog=user_data.get("blog"),
            github_url=user_data.get("html_url"),
            html_url=user_data.get("html_url"),
            public_repos=user_data.get("public_repos", 0),
            public_gists=user_data.get("public_gists", 0),
            followers=user_data.get("followers", 0),
            following=user_data.get("following", 0),
            hireable=user_data.get("hireable", False),
            site_admin=user_data.get("site_admin", False),
            user_type=user_data.get("type", "User"),
            github_created_at=user_data.get("created_at"),
            github_updated_at=user_data.get("updated_at"),
            access_token=user_data.get("access_token"),
            last_login=datetime.now()
        )