from pydantic import BaseModel, field_validator
from typing import List


class CommitUser(BaseModel): 
    login: str

class CommitAuthor(BaseModel): 
    user: CommitUser
    email: str
    name: str


class CommitNode(BaseModel):  
    oid: str
    committedDate: str
    messageHeadline: str
    additions: int
    deletions: int
    changedFiles: int
    url: str
    author: CommitAuthor


class CommitPageInfo(BaseModel): 
    hasNextPage: bool 
    endCursor: str 

class CommitHistory(BaseModel): 
    pageInfo: CommitPageInfo 
    nodes: List[CommitNode] 

class CommitPageInfo(BaseModel): 
    hasNextPage: bool 
    endCursor: str 

class CommitTarget(BaseModel):  
    history: CommitHistory 

class CommitRef(BaseModel):  
    target: CommitTarget 

class CommitRepository(BaseModel):  
    ref: CommitRef 

class CommitData(BaseModel): 
    repository: CommitRepository  
class CommitResponse(BaseModel): 
    data: CommitData 

    @field_validator('data', mode='before')
    @classmethod
    def validate_data(cls, v):
        if not v:
            return None
        return v

class Commit(BaseModel):
    oid: str
    committedDate: str
    messageHeadline: str
    additions: int
    deletions: int
    changedFilesIfAvailable: int
    url: str
    author: CommitAuthor
