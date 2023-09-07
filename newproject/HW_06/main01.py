# Задание №6
# Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.
# ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.
# ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
# ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.
# Создайте модели pydantic для получения новых данных и
# возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление


from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, SecretStr
import databases
import sqlalchemy
from typing import List



DATABASE_URL = "sqlite:///db_s.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


products = sqlalchemy.Table("products",metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Float()),
)


users = sqlalchemy.Table("users",metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(30)),
    sqlalchemy.Column("last_name", sqlalchemy.String(30)),
    sqlalchemy.Column("email", sqlalchemy.String(60)),
    sqlalchemy.Column("password", sqlalchemy.String(20)),
)


orders = sqlalchemy.Table("orders",metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column("product_id", sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column("date_order", sqlalchemy.String(30)),
    sqlalchemy.Column("status_order", sqlalchemy.String(20)),
)


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class ProductIn(BaseModel):
    title: str = Field(max_length=100)
    description: str = Field(max_length=1000)
    price: float

class Product(ProductIn):
    id: int


class UserIn(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    email: EmailStr = Field(max_length=60)
    password: SecretStr = Field(max_length=20)

class User(UserIn):
    id: int


class OrderIn(BaseModel):
    user_id: int = Field(...)
    product_id: int = Field(...)
    date_order: str = Field(max_length= 30)
    status_order: str = Field(max_length=20)

class Order(ProductIn):
    id: int


@app.get('/')
async def get_hello():
    return 'hello world'

@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(first_name=f'user{i}fist', last_name=f'user{i}last', email=f'mail{i}@mail.ru', password=f'{i}pass')
        await database.execute(query)
    return {'message': f'{count} fake users created'}

@app.get("/fake_products/{count}")
async def create_note(count: int):
    for i in range(count):
        query = products.insert().values(title=f'product{i}', description=f'product{i}inorder', price=f'{i}')
        await database.execute(query)
    return {'message': f'{count} fake products created'}

async def check_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)

@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post('/add_orders/', response_model=Order)
async def add_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@app.put('/update_order/{order_id}', response_model=Order)
async def update_order(new_order: OrderIn, order_id: int):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@app.delete('/delete_order/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "order deleted"}


@app.get('/products/', response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)

@app.get('/products/{product_id}', response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.post('/product/', response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.model_dump())
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


@app.put('/products/{product_id}', response_model=Product)
async def update_product(new_product: ProductIn, product_id: int):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), "id": product_id}


@app.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {"message": "product deleted"}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/add_user/', response_model=User)
async def add_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    password = user.password.get_secret_value()
    query = query.values(password=password)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put('/update_users/{user_id}', response_model=User)
async def update_user(new_user: UserIn, user_id: int):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    password = new_user.password.get_secret_value()
    query = query.values(password=password)
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "user deleted"}


# if __name__ == '__main__':
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# uvicorn HW_06.main:app --reload

