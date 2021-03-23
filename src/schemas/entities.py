from typing import Optional

from pydantic import BaseModel


# Shared properties
class EntitiesBase(BaseModel):
    Criterion_ID: int
    Criterion_Name: Optional[str] = None


# Properties to receive on item creation
class EntitiesBaseCreate(EntitiesBase):
    ID: int


# Properties to receive on item update
class EntitiesBaseUpdate(EntitiesBase):
    pass


# Properties shared by models stored in DB
class EntitiesInDBBase(EntitiesBase):
    Criterion_ID: int
    Criterion_Name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Entities(EntitiesInDBBase):
    pass


# Properties properties stored in DB
class EntitiesInDB(EntitiesInDBBase):
    pass
