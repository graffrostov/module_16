from fastapi import FastAPI
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
async def welcome_user(user_id: int) -> str:
    """
       Возвращает приветствие для обычного пользователя
    """
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def user_info(username: str = 'Nik', age: int = 44) -> str:
    """
       Возвращает информацию о пользователе.
       - **username**: имя пользователя, значение по умолчанию 'Nik'
       - **age**: Возраст пользователя, значение по умолчанию 44
    """

    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'