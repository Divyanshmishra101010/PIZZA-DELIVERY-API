from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app import schemas

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/me", response_model=schemas.UserOut)
def read_users_me(current_user: schemas.UserOut = Depends(get_current_user)):
    return current_user
