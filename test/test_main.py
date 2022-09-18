from uuid import uuid4, UUID
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "message": "Service running successfully",
        "data": {}
    }


## USER TEST

response_user = client.post(
        "/api/v1/user",
        headers={"Content-Type": "application/json"},
        json={
            "firstName": "Kevin",
            "lastName": "Ore",
            "email": "test@test.com",
            "yearsPreviousExperience": 6,
            "skills": [
                {
                    "Python": 6
                },
                {
                    "NoSQL": 3
                },
                {
                    "SQL": 4
                },
                {
                    "GIT": 3
                }
            ]
        },
    )


def test_create_user():
    assert response_user.status_code == 201
    assert response_user.json() == {
        "success": True,
        "message": "User created successfully",
        "data": {
            "uuid": response_user.json()["data"]["uuid"],
            "email": "test@test.com"
        }
    }


def test_get_user_by_uuid():
    result = client.get(
        "/api/v1/user?uuid=" + response_user.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"}
    )
    assert result.status_code == 200
    assert result.json() == {
        "success": True,
        "message": "User information",
        "data": [
            {
                "uuid": response_user.json()["data"]["uuid"],
                "firstName": "Kevin",
                "lastName": "Ore",
                "email": "test@test.com",
                "yearsPreviousExperience": "6",
                "skills": [
                    {
                        "Python": 6
                    },
                    {
                        "NoSQL": 3
                    },
                    {
                        "SQL": 4
                    },
                    {
                        "GIT": 3
                    }
                ]
            }
        ]
    }


def test_update_user_by_uuid():
    result = client.put(
        "/api/v1/user/" + response_user.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"},
        json={
            "firstName": "Kevin",
            "lastName": "Ore",
            "email": "test@test.com",
            "yearsPreviousExperience": 6,
            "skills": [
                {
                    "Python": 6
                },
                {
                    "NoSQL": 3
                },
                {
                    "SQL": 4
                },
                {
                    "GIT": 3
                }
            ]
        }
    )
    assert result.status_code == 202
    assert result.json() == {
        "success": True,
        "message": "User updated successfully",
        "data": {
            "uuid_reference": response_user.json()["data"]["uuid"],
            "updated": 1
        }
}


## JOB TEST

response_job = client.post(
        "/api/v1/job",
        headers={"Content-Type": "application/json"},
        json={
            "positionName": "Python Dev",
            "companyName": "Test company",
            "salary": 9999999,
            "currency": "COP",
            "vacancyLink": "https://www.test.com",
            "requiredSkills": [
                {
                    "Python": 6
                },
                {
                    "NoSQL": 3
                },
                {
                    "SQL": 4
                },
                {
                    "GIT": 3
                }
            ]
        }
    )


def test_create_job():
    assert response_job.status_code == 201
    assert response_job.json() == {
        "success": True,
        "message": "Job created successfully",
        "data": {
            "uuid": response_job.json()["data"]["uuid"],
            "companyName": "Test company",
            "positionName": "Python Dev"
        }
    }


def test_get_job_by_uuid():
    result = client.get(
        "/api/v1/job?uuid=" + response_job.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"}
    )
    assert result.status_code == 200
    assert result.json() == {
        "success": True,
        "message": "Job information",
        "data": [
            {
                "uuid": response_job.json()["data"]["uuid"],
                "positionName": "Python Dev",
                "companyName": "Test company",
                "salary": 9999999,
                "currency": "COP",
                "vacancyLink": "https://www.test.com",
                "requiredSkills": [
                    {
                        "Python": 6
                    },
                    {
                        "NoSQL": 3
                    },
                    {
                        "SQL": 4
                    },
                    {
                        "GIT": 3
                    }
                ]
            }
        ]
    }


def test_update_job_by_uuid():
    result = client.put(
        "/api/v1/job/" + response_job.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"},
        json={
            "positionName": "Python Dev",
            "companyName": "Test company",
            "salary": 9999999,
            "currency": "COP",
            "vacancyLink": "https://www.test.com",
            "requiredSkills": [
                {
                    "Python": 6
                },
                {
                    "NoSQL": 3
                },
                {
                    "SQL": 4
                },
                {
                    "GIT": 3
                }
            ]
        }
    )
    assert result.status_code == 202
    assert result.json() == {
        "success": True,
        "message": "Job updated successfully",
        "data": {
            "uuid_reference": response_job.json()["data"]["uuid"],
            "updated": 1
        }
    }


## FILTER JOB BY USER SKILLS

def test_filter_job_by_user_uuid():
    result = client.get(
        "/api/v1/job/filter/" + response_user.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"}
    )
    assert result.status_code == 200


def test_delete_user_by_uuid():
    result = client.delete(
        "/api/v1/user/delete/" + response_user.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"}
    )
    assert result.status_code == 202
    assert result.json() == {
        "success": True,
        "message": "User deleted successfully",
        "data": {
            "uuid": response_user.json()["data"]["uuid"]
        }
    }


def test_delete_job_by_uuid():
    result = client.delete(
        "/api/v1/job/delete/" + response_job.json()["data"]["uuid"],
        headers={"Content-Type": "application/json"}
    )
    assert result.status_code == 202
    assert result.json() == {
        "success": True,
        "message": "Job deleted successfully",
        "data": {
            "uuid": response_job.json()["data"]["uuid"]
        }
    }


