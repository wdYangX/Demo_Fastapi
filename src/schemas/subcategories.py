from typing import Optional

from pydantic import BaseModel


class SubCategoriesBase(BaseModel):
    ID: Optional[int] = None
    SubCategories_name: Optional[str] = None
    Cat_ID: Optional[str] = None


# Properties to receive on item creation
class SubCategoriesCreate(BaseModel):
    ID: int


# Properties to receive on item update
class SubCategoriesUpdate(BaseModel):
    pass


# Properties shared by models stored in DB
class SubCategoriesInDBBase(SubCategoriesBase):
    ID: int
    SubCategories_name: str
    Cat_ID: int

    class Config:
        orm_mode = True


# Properties to return to client
class SubCategories(SubCategoriesInDBBase):
    pass


# Properties properties stored in DB
class SubCategoriesInDB(SubCategoriesInDBBase):
    pass
