"""
    User pydantic models
"""

from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
        User pydantic model

        :param uuid: User UUID
        :param first_name: User first name
        :param last_name: User last name
        :param email: User email
    """
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    email: EmailStr = Field(..., example="john@email.com")


class UserReadSchema(UserSchema):
    """
        User pydantic model

        :param uuid: User UUID
        :param first_name: User first name
        :param last_name: User last name
        :param email: User email
    """
    uuid: UUID
