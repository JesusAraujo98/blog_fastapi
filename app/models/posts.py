from pydantic import BaseModel
from typing import Optional
from app.config.db import conn

class Post(BaseModel):
    book:str
    author:str
    categories:list[str]
    body:list[str]
    rate:int
    
    def save(self):
        id = conn.local.posts.insert_one(dict(self)).inserted_id
        return id


