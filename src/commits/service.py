from fastapi import FastAPI
import httpx 
import os
from datetime import datetime
from src.graphql.queries.commit_queries import get_commits_by_date
import ipdb
from dotenv import load_dotenv
import json 
from src.commits.model import Commit, CommitNode, CommitResponse
from typing import List
load_dotenv()

class CommitService:
    def __init__(self, repo_id: str, owner: str, author_email: str, start_date: str, end_date: str, branch: str):
        self.repo_id = repo_id
        self.owner = owner
        self.author_email = author_email 
        self.start_date = start_date if start_date else "2025-01-01"
        self.end_date = end_date if end_date else "2025-12-31"
        self.branch = branch if branch else "main"

    async def get_commits_by_date(self):
        response_data = await self._get_commits()
        return self._format_commits(response_data)


    async def _get_commits(self):
        url = self._graphql_url()
        query = self._get_commits_query()
        payload = {"query": query}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, 
                headers={"Authorization": f"token {self._personal_access_token()}"}, 
                json=payload 
            )
        return response.json()

    def _get_commits_query(self):
        return get_commits_by_date(
            author_email=self.author_email, 
            start_date=self.start_date, 
            end_date=self.end_date, 
            repo_name=self.repo_id, 
            repo_owner=self.owner, 
            branch=self.branch)
    
    def _graphql_url(self):
        return f"https://api.github.com/graphql"

    def _personal_access_token(self):
        return os.getenv("GITHUB_TOKEN")
    
    def _client(self):
        return httpx.Client()
    

    def _format_commits(self, response_data):
        commit_response = CommitResponse(**response_data)
        nodes = commit_response.data.repository.ref.target.history.nodes
        return [node.model_dump() for node in nodes]