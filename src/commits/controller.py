from src.commits.service import CommitService 
from fastapi import APIRouter
router = APIRouter(
    prefix="/api/v1/commits",
    tags=["commits"]
)
@router.get("/")
async def get_commits(repo_id: str, owner: str, author_email: str, start_date: str, end_date: str, branch: str):
    commit_service = CommitService(repo_id, owner, author_email, start_date, end_date, branch)
    commits =  await commit_service.get_commits_by_date()
    return commits