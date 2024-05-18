from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

# Part 8 -> Body-Fields


class Item(BaseModel):
    name: str
    description: str | None = Field(
        ..., title="It is description of descriptoin", max_length=5
    )


@app.post("/items/{item_id}")
async def post_items(item_id: int, item: Item = Body(..., embed=True)):
    results = {"itemd_id": item_id, "item": item}
    return results
