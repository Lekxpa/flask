from pydantic import BaseModel, Field, EmailStr, SecretStr
import pydantic
from datetime import datetime

class ProductIn(BaseModel):
    title: str = Field(max_length=100)
    description: str = Field(max_length=1000)
    price: float

class Product(ProductIn):
    id: int


class UserIn(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    email: pydantic.EmailStr = Field(max_length=60)
    password: pydantic.SecretStr = Field(max_length=20)

class User(UserIn):
    id: int

from datetime import date

class OrderIn(BaseModel):
    user_id: int = Field(...)
    product_id: int = Field(...)
    date_order: date = Field(..., format="%Y.%m.%d")
    status_order: str = Field(max_length=20)

class Order(ProductIn):
    id: int