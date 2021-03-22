import json

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import Response

from src import schemas
from src.models import Categories, SubCategories, Pros, Hashtag


router = APIRouter()


@router.get(
    '/users'
)
async def list_pros(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
        environment: str = Depends(),
):
    users = get_multi(db, skip=skip, limit=limit, environment=environment)
    if not users:
        return Response(json.dumps({
            "messageCode": codes['db'],
            "message": ptBr['eNotAnyUsers']
        }),
            status_code=404)

    return users