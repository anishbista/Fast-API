from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

# Part 8 -> Body-Fields


class Item(BaseModel):
    name: str
    description: str | None = Field(
        ..., title="It is description of descriptoin", max_length=5
    )
    tags: list[int]
    # tags: set = set()


@app.post("/items/{item_id}")
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
