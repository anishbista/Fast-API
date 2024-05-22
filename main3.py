from typing import Literal
from fastapi import (
    Body,
    Cookie,
    Depends,
    FastAPI,
    Form,
    HTTPException,
    Header,
    Path,
    Query,
)
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2,
    },
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": [],
    },
}


@app.get("/items/{item_id}", response_model=Item)
async def read_items(item_id: str):
    return items.get(item_id)


@app.put("/items/{item_id}", response_model=Item)
async def update_items(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@app.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: str, item: Item):
    stored_item_data = items.get(item_id)
    if stored_item_data:
        stored_item_model = Item(**stored_item_data)
    else:
        stored_item_model = Item()

    print(stored_item_model)
    update_data = item.model_dump(
        exclude_unset=True
    )  # exclude_unset=True exclude all fields that is unset while post request
    print(update_data)
    updated_item = stored_item_model.model_copy(update=update_data)
    print(updated_item)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


# Part 22 - Dependencies Intro


async def hello():
    return "hello"


async def common_parameters(
    q: str | None = None, skip: int = 0, limit: int = 100, blah: str = Depends(hello)
):
    return {"q": q, "skip": skip, "limit": limit, "hello": blah}


@app.get("/items/")
async def get_items(commons: dict = Depends(common_parameters)):
    return commons


# Part 23 - Classes as Dependencies

fake_items_db = [{"item_name": "apple"}, {"item_name": "banana"}]


class CommonQueryParams:
    def __init__(
        self,
        apple: str | None = Query(None),
        q: str | None = None,
        skip: int = 0,
        limit: int = 100,
    ):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.post("/items_list/")
async def get_items_list(commons=Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


# Part 25 -> Dependencies in path operation decorators


async def verify_token(x_token: str = Header(...)):
    if x_token != "anish":
        raise HTTPException(status_code=400, detail="Wrong token")


async def verify_key(x_key: str = Header(...)):
    if x_key != "bista":
        raise HTTPException(status_code=400, detail="Wrong key")


# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])      #This will implement dependencies in all routes


@app.get(
    "/products/",
)
async def read_items():
    return [{"item": "Foo"}]


@app.get("/users/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
