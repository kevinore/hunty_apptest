from uuid import uuid4
from datetime import datetime
from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    UUIDField,
    ListField,
    IntField
)


class MetaModel:
    uuid = UUIDField(
        default=uuid4,
        binary=False,
        unique=True
    )
    created_at = DateTimeField(
        default=datetime.now(),
    )
    updated_at = DateTimeField(
        default=datetime.now(),
        null=True
    )


class User(Document, MetaModel):
    firstName = StringField(
        title="First Name of user",
        required=True
    )
    lastName = StringField(
        title="last Name of user",
        required=True
    )
    email = StringField(
        title="Email of user",
        required=True
    )
    yearsPreviousExperience = StringField(
        title="Years previous experience",
        required=True
    )
    skills = ListField(
        title="Skills of user",
        required=True
    )

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Kevin",
                "lastName": "Ore",
                "email": "kevin@example.com",
                "yearsPreviousExperience": 5,
                "skills": [
                        {
                            "python": 1
                        },
                        {
                            "nosql": 2
                        }
                ]
            }
        }


class Job(Document, MetaModel):
    positionName = StringField(
        title="Position name",
        required=True
    )
    companyName = StringField(
        title="Company Name of job",
        required=True
    )
    salary = IntField(
        title="Salary of job",
        required=True
    )
    currency = StringField(
        title="Years previous experience",
        required=True
    )
    vacancyLink = StringField(
        title="Vacancy link of job",
        required=True
    )
    requiredSkills = ListField(
        title="Skills of user",
        required=True
    )

    class Config:
        schema_extra = {
            "example": {
                "positionName": "Python Dev",
                "companyName": "Test company",
                "Salary": 9999999,
                "currency": "COP",
                "vacancyLink": "https://www.test.com",
                "requiredSkills": [
                        {
                            "Python": 1
                        },
                        {
                            "NoSQL": 2
                        }
                ]
            }
        }