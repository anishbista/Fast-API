from typing import Optional
from fastapi import Body, FastAPI, Path, Query
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


# @app.get("/", description="This is just practice", deprecated=False)
# async def root():
#     return {"message": "Hello Worldsasd"}


# @app.post("/")
# async def post():
#     return {"message": "Hello from the post "}


# @app.put("/put")
# async def put():
#     return {"message": "This is put method"}


# @app.get("/items/me")
# async def get_items():
#     return {"message": "This is test"}


# @app.get("/items/{id}")
# async def list_items(id: str):
#     print("dadadads", type(id))
#     if not isinstance(id, str):
#         return {"message": "please enter"}
#     else:
#         return {"id": id}


# class FoodEnum(str, Enum):
#     vegatables = "cauli"
#     fruits = "apple"


# @app.get("/food_items/{name}")
# async def food_items(name: FoodEnum):
#     if name == FoodEnum.vegatables:
#         return {"message": "it is vegatbles"}
#     else:
#         return {"message": "It is fruits"}


# items_db = [{"name": "apple"}, {"name": "mango"}, {"name": "banana"}]


# @app.get("/products")
# async def product_list(skip: int = 0, limit: int = 10):
#     return items_db[skip : skip + limit]


# @app.get("/products/{product_id}")
# async def get_product(
#     product_id: int, anish: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": product_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"descriptin": "asdsasdad dadad addada adadsa "})
#     return item


# class Item(BaseModel):
#     name: str
#     price: int
#     description: str | None = None
#     tax: float | None = None


# @app.post("/item")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     item_dict.update({"sdadsad": "anish"})
#     print(item_dict)
#     return item_dict


# @app.put("/item/{id}")
# async def create_item_with_put(id: int, item: Item):
#     result = {"item_id": id, **item.model_dump()}
#     return result


# @app.get(
#     "/item",
#     description="dsadsadasd",
#     # tags="app",
#     name="dsadadad",
#     response_description="dsadsad",
#     status_code=500,
# )
# # async def read_items(q: str = Query(..., max_length=25, min_length=3)):   ... This will make it required with specifying any default value
# async def read_items(
#     q: list[str] | None = Query(
#         ["sda", "sda"],
#         deprecated=True,
#     )
# ):
#     # async def read_items(q: str | None = Query(None)):
#     results = {"anish": "bista", "q": q}
#     return results


# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#     *,  # In Python, the * (asterisk) symbol in a function parameter list indicates that all subsequent parameters must be specified using keyword arguments. This is known as "keyword-only" arguments.
#     item_id: int = Path(..., title="The id of the item to get", gt=50),
#     q: str,
# ):

#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# Body Multiple Parameters


class Item(BaseModel):
    name: str
    price: float


class User(BaseModel):
    name: str


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The id of the", ge=0, le=150),
    q: str | None = None,
    item: Item | None = None,
    # item: Item = Body(..., embed=True),  this will ask to pass as key value pair instead of default like {
    #   "item": {
    #     "name": "string",
    #     "price": 0
    #   }
    # }  instead of  {
    # "name": "string",
    # "price": 0
    # }
    user: User | None = None,
    importance: int = Body(...)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results
