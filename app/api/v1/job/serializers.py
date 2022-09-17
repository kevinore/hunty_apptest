from pydantic import BaseModel, Field
from typing import List


class Job(BaseModel):
    positionName: str = Field(
        title="Position of job",
        default=None
    )
    companyName: str = Field(
        title="Company name of job",
        default=None
    )
    salary: int = Field(
        title="Salary of job",
        default=None
    )
    currency: str = Field(
        title="Currency of job",
        default=None
    )
    vacancyLink: str = Field(
        title="Vacancy link of job",
        default=None
    )
    requiredSkills: List = Field(
        title="Required skills of job",
        default=None
    )
