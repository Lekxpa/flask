from pydantic import BaseModel, Field
class User(BaseModel):
    name: str = Field(max_length=10)

# Field импортируется непосредственно из pydantic, а не из
# fastapi как для всех остальных (Query, Path и т.д.).
