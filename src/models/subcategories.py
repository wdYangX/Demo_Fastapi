from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .subcategories import SubCategories  # noqa: F401


class SubCategories(Base):
    ID = Column(Integer, primary_key=True, index=True)
    SubCat_name = Column(String, index=True)
    Cat_ID = Column(String, ForeignKey("Categories.ID"), index=True)

