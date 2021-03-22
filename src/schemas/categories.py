from typing import Optional

from pydantic import BaseModel


# Shared properties
class CategoriesBase(BaseModel):
    ID: Optional[str] = None
    Cat_name: Optional[str] = None
    Pros_ID: Optional[str] = None


# Properties to receive on item creation
class CategoriesBaseCreate(CategoriesBase):
    ID: int


# Properties to receive on item update
class CategoriesBaseUpdate(CategoriesBase):
    pass


# Properties shared by models stored in DB
class CategoriesInDBBase(CategoriesBase):
    ID: int
    Cat_name: str
    Pros_ID: int

    class Config:
        orm_mode = True


# Properties to return to client
class Categories(CategoriesInDBBase):
    pass


# Properties properties stored in DB
class CategoriesInDB(CategoriesInDBBase):
    pass
