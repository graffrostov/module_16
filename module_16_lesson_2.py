from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
import asyncio

app = FastAPI()

@app.get("/")
async def main_page() -> str:
    """
       Возвращает приветствие главной страницы
    """
    return 'Главная страница'

@app.get("/user/admin")
async def welcome_admin() -> str:
    """
       Возвращает приветствие для администратора
    """
    return 'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def welcome_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    """
       Возвращает приветствие для обычного пользователя
    """
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def user_info(

        username: Annotated[str,
        Path(min_length=5,
             max_length=20,
             description='Enter username',
             example='UrbanUser')],

        age: Annotated[int,
        Path(ge=18,
             le=120,
             description='Enter age',
             example=24)]
        ) -> str:

    """
       Возвращает информацию о пользователе.
       - **username**: имя пользователя
       - **age**: Возраст пользователя
    """

    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'