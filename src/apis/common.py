from typing import Generator

from fastapi import Depends, HTTPException, status
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src import  models, schemas
from src.core.config import settings
from src.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()