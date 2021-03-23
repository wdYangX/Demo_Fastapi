from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .categories import Categories  # noqa: F401


class Categories(Base):
    ID = Column(Integer, primary_key=True, index=True)
    Cat_name = Column(String, index=True)
    Pros_ID = Column(Integer, ForeignKey("Pros.ID"))
    # cat = relationship("Pros", back_populates="pros")