from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None # необязательные данные
    price: float # обязательные данные
    tax: Optional[float] = None