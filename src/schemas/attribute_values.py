from typing import Optional

from pydantic import BaseModel


# Shared properties
class AttributeValuesBase(BaseModel):
    Value_ID: int
    Criterion_ID: int
    Attribute_ID: int
    Value: Optional[str] = None


# Properties to receive on item creation
class AttributeValuesBaseCreate(AttributeValuesBase):
    Value_ID: int


# Properties to receive on item update
class AttributeValuesBaseUpdate(AttributeValuesBase):
    pass


# Properties shared by models stored in DB
class AttributeValuesInDBBase(AttributeValuesBase):
    Value_ID: int
    Criterion_ID: int
    Attribute_ID: int
    Value: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to return to client
class AttributeValues(AttributeValuesInDBBase):
    pass


# Properties properties stored in DB
class AttributeValuesInDB(AttributeValuesInDBBase):
    pass
