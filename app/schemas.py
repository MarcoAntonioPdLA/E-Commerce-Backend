from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    title: str
    price: float
    description: Optional[str] = None
    image: Optional[str] = None
    category: str

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"