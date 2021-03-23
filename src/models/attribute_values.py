from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .attribute_values import AttributeValues  # noqa: F401


class AttributeValues(Base):
    Value_ID = Column(Integer, primary_key=True, index=True)
    Criterion_ID = Column(Integer, ForeignKey('entities.Criterion_ID'))
    Attribute_ID = Column(Integer, ForeignKey('attributes.Attribute_ID'))
    Value = Column(String, index=True)

    entity = relationship("Entities", back_populates="attr_val")
    attribute = relationship("AttributeValues", back_populates="attr_val")
