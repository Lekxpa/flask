from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def read_root():
    return {'Ytllo': "world"}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, 'q': q}
    return {'item_id': item_id}


@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
# обработка данных
    return {"user_id": user_id, "order_id": order_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}



@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)

templates = Jinja2Templates(directory="./seminar05/templates")
@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})

