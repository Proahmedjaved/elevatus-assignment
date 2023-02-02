"""
    User pydantic models
"""

from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from utilities import LowerCaseEmailStr


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
    email: LowerCaseEmailStr = Field(..., example="john@email.com")
    password: str = Field(..., example="password")


class UserReadSchema(UserSchema):
    """
        User pydantic model

        :param uuid: User UUID
        :param first_name: User first name
        :param last_name: User last name
        :param email: User email
    """
    uuid: UUID
    password: str = None