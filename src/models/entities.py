from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .entities import Entities  # noqa: F401


class Entities(Base):
    Criterion_ID = Column(Integer, primary_key=True, index=True)
    Criterion_Name = Column(String, index=True)

    attr_val = relationship("AttributeValues", backref="entity")