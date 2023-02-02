"""
This file contains the routers for the API.
"""

from fastapi import APIRouter
from routers import user
from routers import candidate
from routers import auth

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(candidate.router, prefix="/candidate", tags=["candidate"])
