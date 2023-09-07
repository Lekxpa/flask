from fastapi import APIRouter
from newproject.HW_06.works_files.models import Order, OrderIn
from typing import List
from newproject.HW_06.works_files.dbs import orders, database


router = APIRouter()
# app = FastAPI()

@router.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.post('/order/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@router.put('/orders/{order_id}', response_model=Order)
async def update_order(new_order: OrderIn, order_id: int):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@router.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "order deleted"}