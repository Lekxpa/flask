# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Реализуйте валидацию данных запроса и ответа.

# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
# удалять информацию о пользователе из базы данных
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из
# списка.

import pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, SecretStr
# import uvicorn

app = FastAPI()

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
@app.get('/users/')
async def all_users():
    return {'users': USERS}


@app.post('/user/add')
async def add_user(user: User):
    USERS.append(user)
    return {'user': user, 'status': 'added'}

@app.put('/user/update/{user_id}')
async def update_user(user_id: int, user: User):
    for u in USERS:
        if u.id_ == user_id:
            u.id_ = user.id_
            u.name = user.name
            u.email = user.email
            u.password = user.password
            return {'user': user, 'status': 'updated'}
    return HTTPException(404, "user not found")


@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: int):
    for u in USERS:
        if u.id_ == user_id:
            USERS.remove(u)
            return {'status': 'deleted'}
    return HTTPException(404, 'user not found')




# if __name__ == "__main__":
#     uvicorn.run("main04_05:app", port=8000)