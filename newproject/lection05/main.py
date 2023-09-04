#
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# В этом примере мы создали объект FastAPI и определили конечную точку API с
# помощью декоратора @app.get("/"). Декоратор указывает, что это обработчик
# GET-запроса по пути "/".
# Внутри функции мы возвращаем словарь с сообщением "Hello World". Это
# сообщение будет отправлено в ответ на запрос.

# Для запуска приложения необходимо использовать сервер для запуска приложений
# uvicorn. Для этого открываем терминал ОС, переходим в каталог с проектом и
# выполняем следующую команду:
# uvicorn main:app --reload

import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()



class Item(BaseModel):
    name: str
    description: Optional[str] = None # необязательные данные
    price: float # обязательные данные
    tax: Optional[float] = None
@app.get('/')
async def read_root():
    logger.info('отработал GET запрос')
    return {'hello'}

@app.post('/items/')
async def create_item(item: Item):
    logger.info('Отработал POST запрос')
    return item

@app.put('/item/{item_id') #изменяем данные
async def update_item(item_id: int, item: Item):
    logger.info(f'отработал PUT запрос для item-id = {item_id}')
    return {'item_ed':item_id, 'item': item}

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'отработал DELETE запрос для item-id = {item_id}')
    return {'item_ed': item_id}