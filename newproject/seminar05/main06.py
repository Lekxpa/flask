# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import pydantic
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel, EmailStr, SecretStr
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="./seminar05/templates")

USERS = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


USERS.append(User(id_=1,
                    name='Mikle',
                    email='mikle@gmail.com',
                    password='12345'))
USERS.append(User(id_=2,
                    name='Niki',
                    email='niki@gmail.com',
                    password='54321'))
USERS.append(User(id_=3,
                    name='Kate',
                    email='kate@gmail.com',
                    password='12354'))


@app.get("/", response_class=HTMLResponse)
async def users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': USERS})


@app.post('/user/add')
async def add_user(id_=Form(), name=Form(), email=Form(), password=Form()):
    USERS.append(User(id_=id_, name=name, email=email, password=password))
    return RedirectResponse('/', status_code=302)