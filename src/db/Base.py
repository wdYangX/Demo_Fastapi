# Import all the models, so that Base has them before being
# imported by Alembic
from src.db.base_class import Base  # noqa
from src.models.pros import Pros # noqa
from src.models.categories import Categories  # noqa
from src.models.subcategories import SubCategories  # noqa
from src.models.hashtag import Hashtag  # noqa