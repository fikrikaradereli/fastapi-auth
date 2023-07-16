from typing import Annotated
from fastapi import APIRouter, Depends
from app import schemas
from .dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me", response_model=schemas.User)
def read_user_me(current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return current_user
