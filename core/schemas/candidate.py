"""
    Candidate pydantic models
"""

from uuid import UUID
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from utilities import LowerCaseEmailStr


class CareerLevel(str, Enum):
    """
        Career level enum
    """
    JUNIOR = "Junior"
    SENIOR = "Senior"
    MANAGER = "Manager"

class Gender(str, Enum):
    """
        Gender enum
    """
    MALE = "MALE"
    FEMALE = "FEMALE"
    NOT_SPECIFIED = "NOT_SPECIFIED"



class CandidateSchema(BaseModel):
    """
        Candidate pydantic model

    """
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    email: LowerCaseEmailStr = Field(..., example="john@email.com")
    career_level: CareerLevel = Field(..., example="Junior")
    job_major: str = Field(..., example="Computer Science")
    years_of_experience: int = Field(..., example=1)
    degree_type: str = Field(..., example="Bachelor")
    skills: list = Field(..., example=["Python", "Django"])
    nationality: str = Field(..., example="Egyptian")
    city: str = Field(..., example="Cairo")
    salary: int = Field(..., example=1000)
    gender: Gender = Field(..., example="MALE")


class CandidateReadSchema(CandidateSchema):
    """
        User pydantic model

        :param uuid: User UUID
        :param first_name: User first name
        :param last_name: User last name
        :param email: User email
    """
    uuid: UUID


class CandidateUpdateSchema(BaseModel):
    """
        Candidate update pydantic model
    """

    first_name: Optional[str] = Field(..., example="John")
    last_name: Optional[str] = Field(..., example="Doe")
    email: Optional[EmailStr] = Field(..., example="")
    career_level: Optional[CareerLevel] = Field(..., example="Junior")
    job_major: Optional[str] = Field(..., example="Computer Science")
    years_of_experience: Optional[int] = Field(..., example=1)
    degree_type: Optional[str] = Field(..., example="Bachelor")
    skills: Optional[list] = Field(..., example=["Python", "Django"])
    nationality: Optional[str] = Field(..., example="American")
    city: Optional[str] = Field(..., example="New York")
    salary: Optional[int] = Field(..., example=1000)
    gender: Optional[Gender] = Field(..., example="Male")
