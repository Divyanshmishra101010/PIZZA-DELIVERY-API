from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, schemas, crud, auth, models

router = APIRouter(prefix="/order", tags=["order"])

@router.post("/", response_model=schemas.OrderOut)
def create_new_order(order: schemas.OrderCreate, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_order(db, order, current_user.id)

@router.get("/pizzas", response_model=list[schemas.PizzaOut])
def list_all_pizzas(db: Session = Depends(database.SessionLocal)):
    return crud.list_pizzas(db)
