from fastapi import APIRouter, Depends, Response, status, UploadFile, File
import os
import json
from bson.objectid import ObjectId
from app.config.db import conn
from app.models.posts import Post
from app.schemas.posts import postEntity, postsEntity

posts = APIRouter()

@posts.get('/api/posts/delete', tags=['posts'])
async def delete_all_posts():
    conn.local.posts.drop()
    return {'message':'ok'}


@posts.get('/api/posts/<id>', tags=['posts'], status_code=200)
async def get_single_post(id:str):
    try:
        data = postEntity(conn.local.posts.find_one({'_id':ObjectId(id)}))
        return data
    except:
        status.status_code = status.HTTP_404_NOT_FOUND
        return {'message':'something went wrong'}


@posts.get('/api/posts', tags=['posts'], status_code=200)
async def posts_get():
    try:
        data = postsEntity(conn.local.posts.find())
    except:
        data = {'message':"something went wrong"}
        status.status_code = status.HTTP_404_NOT_FOUND
    return data


@posts.post('/api/posts/', tags=['posts'], status_code=201)
async def posts_save(new_post:Post):
    try:
        id = new_post.save()
        return {'message':'ok'}
    except:
        status.status_code = status_HTTP_400_BAD_REQUEST
        return {'message':"something went wrong"}
