from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .hashtag import Hashtag  # noqa: F401


class Hashtag(Base):
    ID = Column(Integer, primary_key=True, index=True)
    Hashtag_name = Column(String, index=True)
    Pros_ID = Column(Integer, ForeignKey("SubCategories.ID"))
    # SubCat_ID = relationship("Item", back_populates="owner")