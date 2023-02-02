import bson
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from uuid import uuid4, UUID
from core.schemas import UserSchema, UserReadSchema
from core.database import users

router = APIRouter()

@router.post("/")
async def create_user(user: UserSchema) -> UserReadSchema:
    """
    Create a new user.

    - **first_name**: User first name (required)
    - **last_name**: User last name (required)
    - **email**: User email (required)

    """
    uuid = bson.Binary.from_uuid(uuid4())
    document = {"uuid": uuid, **user.dict()}
    users.insert_one(document)
    return document


@router.get("/{uuid}")
async def get_user(uuid: UUID) -> UserReadSchema:
    """
    Get a user by uuid.

    - **uuid**: User uuid (required)
    """
    user = users.find_one({"uuid": bson.Binary.from_uuid(uuid)}, {"_id": 0})
    if user is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
    return user
    