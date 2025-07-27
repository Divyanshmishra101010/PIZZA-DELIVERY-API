from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes  = True

class PizzaOut(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes  = True

class OrderCreate(BaseModel):
    pizza_id: int
    quantity: int

class OrderOut(BaseModel):
    id: int
    pizza_id: int
    quantity: int
    user_id: int

    class Config:
        from_attributes  = True
