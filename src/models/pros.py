from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .pros import Pros  # noqa: F401


class Pros(Base):
    id = Column(Integer, primary_key=True, index=True)
    Firstname = Column(String, index=True)
    Lastname = Column(String, index=True)
    # pros = relationship("Categories", back_populates="cat")