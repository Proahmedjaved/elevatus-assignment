"""
    User router.

"""

from uuid import uuid4, UUID
import bson
from fastapi import APIRouter, status, Security
from fastapi.responses import JSONResponse
from passlib.hash import pbkdf2_sha256
from core.schemas import UserSchema, UserReadSchema
from core.database import users
from core.security import get_current_active_user

router = APIRouter()

@router.post("/", response_model_exclude_defaults=True)
async def create_user(user: UserSchema) -> UserReadSchema:
    """
    Create a new user.

    - **first_name**: User first name (required)
    - **last_name**: User last name (required)
    - **email**: User email (required)

    """

    # Check if user exists
    if users.find_one({"email": user.email}):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, 
            content={"message": "User already exists"}
            )

    user.password = pbkdf2_sha256.hash(user.password)

    uuid = bson.Binary.from_uuid(uuid4())
    document = {"uuid": uuid, **user.dict()}
    users.insert_one(document)

    del document["password"]

    return document


@router.get("/{uuid}", response_model_exclude_defaults=True)
async def get_user(uuid: UUID, current_user = Security(get_current_active_user)) -> UserReadSchema:
    """
    Get a user by uuid.

    - **uuid**: User uuid (required)
    """
    if current_user["uuid"] != uuid:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"message": "You are not allowed to access this resource"}
        )

    user = users.find_one({"uuid": bson.Binary.from_uuid(uuid)}, {"_id": 0, "password": 0})
    return user


@router.delete("/{uuid}", 
    response_model_exclude_defaults=True, 
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(uuid: UUID, current_user = Security(get_current_active_user)):
    """
    Delete a user by uuid.

    - **uuid**: User uuid (required)
    """
    if current_user["uuid"] != uuid:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"message": "You are not allowed to access this resource"}
        )

    users.delete_one({"uuid": bson.Binary.from_uuid(uuid)})
