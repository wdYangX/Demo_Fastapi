from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProsBase(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


# Properties to receive via API on creation
class ProsCreate(ProsBase):
    id: int

# Properties to receive via API on update
class ProsUpdate(ProsBase):
    password: Optional[str] = None


class ProsInDBBase(ProsBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Pros(ProsInDBBase):
    pass


# Additional properties stored in DB
class ProsInDB(ProsInDBBase):
    hashed_password: str