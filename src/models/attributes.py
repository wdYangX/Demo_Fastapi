from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .attributes import Attributes  # noqa: F401


class Attributes(Base):
    Attribute_ID = Column(Integer, primary_key=True, index=True)
    Attribute_Name = Column(String, index=True)

    attr_val = relationship("AttributeValues", backref="attribute")