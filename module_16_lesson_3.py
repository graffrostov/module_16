# from email.policy import default
# from pydantic import BaseModel
# import asyncio

from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()



users = {'1': 'Имя: Example, возраст: 18'}

# -----------------------------------------------------------------------------------------------------------
@app.get('/users')
async def get_all_messages() -> dict:
    return users
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str,

        Path(
            min_length=3,
            max_length=20,
            regex="^[a-zA-Z0-9_-]+$",
            description='Enter user name',
            example='New_user')],

        age: Annotated[int,

        Path(
            ge=1,
            le=120,
            description='Enter user age',
            example=18)])\
        -> str:

    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
@app.put('/user/{user_id}/{username}/{age}')
async def update_message(
        user_id:Annotated[str,

        Path(
            regex="^[0-9]+$",
            description='Enter user id',
            example='1')],

        username: Annotated[str,

        Path(
            min_length=3,
            max_length=20,
            regex="^[a-zA-Z0-9_-]+$",
            description='Enter user name',
            example='Change_user')],

        age: Annotated[int,

        Path(
            ge=1,
            le=120,
            description='Enter user age',
            example=18)])\
        -> str:

    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is updated'

    raise HTTPException(status_code=404, detail="Пользователь не найден")
# -----------------------------------------------------------------------------------------------------------

# @app.delete('/user/{user_id}')
# async def delete_message(user_id: str) -> str:
#     users.pop(user_id)
#     return f'User with {user_id} was deleted.'

# -----------------------------------------------------------------------------------------------------------
@app.delete('/user/{user_id}')
async def delete_message(
        user_id: Annotated[str,

        Path(
            regex="^[0-9]+$",
            description='Enter user id',
            example='1')])\
        -> str:
    try:
        users.pop(user_id)
        return f'User {user_id} was deleted.'
    except:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
# -----------------------------------------------------------------------------------------------------------

