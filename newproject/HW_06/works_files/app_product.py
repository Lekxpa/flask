from fastapi import APIRouter
from models import Product, ProductIn
from typing import List
from newproject.HW_06.works_files.dbs import products, database


router = APIRouter()

@router.get('/products/', response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get('/products/{product_id}', response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.model_dump())
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


@router.put('/products/{product_id}', response_model=Product)
async def update_product(new_product: ProductIn, product_id: int):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), "id": product_id}


@router.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {"message": "product deleted"}