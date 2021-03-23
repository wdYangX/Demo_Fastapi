from typing import Optional

from pydantic import BaseModel


# Shared properties
class AttributesBase(BaseModel):
    Attribute_ID: int
    Attribute_Name: Optional[str] = None


# Properties to receive on item creation
class AttributesBaseCreate(AttributesBase):
    ID: int


# Properties to receive on item update
class AttributesBaseUpdate(AttributesBase):
    pass


# Properties shared by models stored in DB
class AttributesInDBBase(AttributesBase):
    Attribute_ID: int
    Attribute_Name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Attributes(AttributesInDBBase):
    pass


# Properties properties stored in DB
class AttributesInDB(AttributesInDBBase):
    pass
