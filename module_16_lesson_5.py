# from email.policy import default
# from symtable import Class
# import asyncio
# from typing import Annotated
# from email.policy import default

from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Annotated

from fastapi import FastAPI, HTTPException, Body, Path, Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory='templates')


app = FastAPI()
users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/', response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(request=request, name='users.html', context={'users': users})

# -----------------------------------------------------------------------------------------------------------
# @app.get('/users')
# async def get_all_users() -> List[User]:
#     return users

@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_all_users(request: Request, user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse(request=request, name='users.html', context={'user': user})
    raise HTTPException(status_code=404, detail='User was not found')
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
@app.post('/user/{username}/{age}')
async def create_user(user: User) -> User:

    user.id = max(usr.id for usr in users) + 1 if users != [] else 1
    users.append(user)
    return user
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      user_name:str = Body(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$"),
                      user_age:int =Body(ge=1, le=120))\
        -> User:

    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = user_name
            edit_user.age = user_age
            return edit_user


    raise HTTPException(status_code=404, detail="User was not found")
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:

    for i, usr in enumerate(users):
        if usr.id == user_id:
            users.pop(i)
            return usr

    raise HTTPException(status_code=404, detail="User was not found")
# -----------------------------------------------------------------------------------------------------------

