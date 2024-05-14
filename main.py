from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/", description="This is just practice", deprecated=False)
async def root():
    return {"message": "Hello Worldsasd"}


@app.post("/")
async def post():
    return {"message": "Hello from the post "}


@app.put("/put")
async def put():
    return {"message": "This is put method"}


@app.get("/items/me")
async def get_items():
    return {"message": "This is test"}


@app.get("/items/{id}")
async def list_items(id: str):
    print("dadadads", type(id))
    if not isinstance(id, str):
        return {"message": "please enter"}
    else:
        return {"id": id}


class FoodEnum(str, Enum):
    vegatables = "cauli"
    fruits = "apple"


@app.get("/food_items/{name}")
async def food_items(name: FoodEnum):
    if name == FoodEnum.vegatables:
        return {"message": "it is vegatbles"}
    else:
        return {"message": "It is fruits"}


items_db = [{"name": "apple"}, {"name": "mango"}, {"name": "banana"}]


@app.get("/products")
async def product_list(skip: int = 0, limit: int = 10):
    return items_db[skip : skip + limit]


@app.get("/products/{product_id}")
async def get_product(
    product_id: int, anish: str, q: str | None = None, short: bool = False
):
    item = {"item_id": product_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"descriptin": "asdsasdad dadad addada adadsa "})
    return item
