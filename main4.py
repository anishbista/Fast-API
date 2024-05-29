from typing import Literal
from fastapi import Body, Depends, FastAPI, Header, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, EmailStr, Field


app = FastAPI()
