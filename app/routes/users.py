from fastapi import APIRouter, Depends, Response, status, Form
from pydantic import EmailStr
from app.config.auth import AuthHandler
from app.config.db import conn
from app.models.users import User
from passlib.hash import sha256_crypt



users = APIRouter()
auth_handler = AuthHandler()


@users.get('/api/users/delete', tags=['users'])
async def delete_all_users():
    conn.local.users.drop()
    return {'messages':'ok'}


@users.get('/api/users/my_user', tags=['users'])
async def my_user(username = Depends(auth_handler.auth_wrapper)):
    return {'user':username}
    

@users.post('/api/users/login', tags=['users'], status_code=200)
async def login(response: Response, email: EmailStr = Form(), password: str = Form()):
    registered_user = conn.local.users.find_one({'email':email})
    if not registered_user or (not auth_handler.verify_password(password, registered_user['password'])):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':'invalid email or password'}

    token = auth_handler.encode_token(registered_user['username'])
    return token


@users.post('/api/users/create_new_user', tags=['users'], status_code=201)
async def create_user(
        response: Response, 
        email:EmailStr = Form(), 
        username:str = Form(),
        password:str = Form(),
        ):
    registered_user = conn.local.users.find_one({'username':username})
    registered_email = conn.local.users.find_one({'password':password})

    if registered_user or registered_email:
        status.status_code = status.HTTP_409_CONFLICT
        return {'message':'email and/or username already exists'}

    user = User(username=username, email=email, password=password)
    user.password = auth_handler.get_password_hash(user.password)

    id = conn.local.users.insert_one(dict(user)).inserted_id
    return {'message':f'welcome{username}'}









