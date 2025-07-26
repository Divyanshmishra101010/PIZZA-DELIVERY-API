from pydantic import BaseModel
from typing import Optional

class Signup(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    isStaff: Optional[bool] = None
    isActive: Optional[bool] = None

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "isStaff": False,
                "isActive": True
            }
        }
    }
