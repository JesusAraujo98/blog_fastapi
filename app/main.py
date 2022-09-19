from fastapi import FastAPI
from app.routes import users, posts

app = FastAPI()
app.include_router(users.users)
app.include_router(posts.posts)

@app.get('/api/')
def hello_world():
    return {'message':'hello world'}
