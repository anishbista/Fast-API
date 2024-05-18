from typing import Literal
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

# Part 8 -> Body-Fields


class Item(BaseModel):
    name: str
    description: str | None = Field(
        ..., title="It is description of descriptoin", max_length=5
    )
    tags: list[int]
    # tags: set = set()


@app.post(
    "/items/{item_id}", response_model=Item
)  # response model gives the schema of return value
async def post_items(item_id: int, item: Item = Body(..., embed=True)):
    results = {"itemd_id": item_id, "item": item}
    return results


# Part 9 -> Body-Nested Models


class Image(BaseModel):
    name: str
    items: list[Item]


@app.post("/product/{item_id}")
async def post_items(item_id: int, image: list[Image] = Body(..., embed=True)):
    results = {"itemd_id": item_id, "image": image}
    return results


@app.post("/test")
async def post_items(
    test: dict[str, str]
):  # ict[str, str] this expects key as str and value also as int
    results = {"itemd_id": test}
    return results


# Part 13 -> Response Model


class UserBase(BaseModel):
    username: str
    email: EmailStr = "apple@gmail.com"
    full_name: str | None = None


class UserIn(UserBase):
    password: str = "sda"


class UserOut(UserBase):
    pass


users = {
    "a": {"username": "anish"},
    "b": {"username": "bista", "email": "a@gmail.com"},
    "d": {"username": "bista", "email": "a@gmail.com", "full_name": "Anish Bista"},
    "e": {
        "username": "bista",
        "email": "a@gmail.com",
        "full_name": "Anish Bista",
        "password": "acs",
    },
}


@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    print(user.model_dump())
    print(type(user))
    # for k,v in user.dic
    return user


@app.get(
    "/user/{id}", response_model=UserIn, response_model_exclude_unset=True
)  # response_model_exclude_unset=True this will exclude the fields which is not populate manually by user
async def read_user(id: Literal["a", "b", "d", "e"]):

    return users[id]


@app.get("/user/{id}/name", response_model=UserIn, response_model_include={"username"})
async def read_user(id: Literal["a", "b", "d", "e"]):

    return users[id]


@app.get(
    "/user/{id}/public", response_model=UserIn, response_model_exclude={"username"}
)
async def read_user(id: Literal["a", "b", "d", "e"]):

    return users[id]
