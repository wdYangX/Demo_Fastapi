from typing import Optional

from pydantic import BaseModel


# Shared properties
class CategoriesBase(BaseModel):
    id: Optional[str] = None
    cat_name: Optional[str] = None
    pros_id: Optional[str] = None


# Properties to receive on item creation
class CategoriesBaseCreate(CategoriesBase):
    id: str


# Properties to receive on item update
class CategoriesBaseUpdate(CategoriesBase):
    pass


# Properties shared by models stored in DB
class CategoriesInDBBase(CategoriesBase):
    id: int
    cat_name: str
    pros_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Categories(CategoriesInDBBase):
    pass


# Properties properties stored in DB
class CategoriesInDB(CategoriesInDBBase):
    pass
