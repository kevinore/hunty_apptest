from mimetypes import init
from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import List


class Users(BaseModel):
    firstName: str = Field(
        title='Name of user',
        default=None
    )
    lastName: str = Field(
        title='Last name of user',
        default=None
    )
    email: str = Field(
        title='Email of user',
        default=None
    )
    yearsPreviousExperience: str = Field(
        title='Years previous experience',
        default=None
    )
    skills: List = Field(
        title='Skills of user',
        default=None
    )
