from uuid import uuid4, UUID
from datetime import datetime
from app.core.exceptions import exception
from app.core.models import User, Job
from app.core.queryset import ModelsQuerys


class ProcessHandler:

    @classmethod
    def create_user(cls, serializer: dict):
        """
        Create users
        """
        orm = ModelsQuerys(User)

        query_user = {
            "email": serializer["email"]
        }

        user = orm.find_by_query(query_user)

        if user:
            exception(
                "User already exists",
                {"email": serializer["email"]},
                409
            )

        serializer["uuid"] = uuid4()
        orm.save(serializer)

        return {"uuid": serializer["uuid"], "email": serializer["email"]}

    @classmethod
    def get_users(cls, **params):
        """
        Get user by any param
        """
        orm = ModelsQuerys(User)
        users = orm.find_by_query(params)
        return list(map(lambda user: cls.__remove_unnecessary_fields(user), users))

    @staticmethod
    def __remove_unnecessary_fields(user):
        user.__delitem__('_id')
        user.__delitem__('updated_at')
        user.__delitem__('created_at')
        return user

    @classmethod
    def update_users(cls, uuid: UUID, serializer: dict):
        """
        Update user
        """
        query_user = {
            "uuid": uuid
        }

        orm = ModelsQuerys(User)
        user = orm.find_by_query(query_user)

        if not user:
            exception(
                "User does not exists",
                {"email": serializer["email"]},
                409
            )

        serializer['updated_at'] = datetime.now()
        user = orm.update_by_query(query_user, serializer)

        return {
            "uuid_reference": uuid,
            "updated": user
        }

    @classmethod
    def delete_users(cls, uuid: UUID):
        """
        Delete user
        """
        query_user = {
            "uuid": uuid
        }

        orm = ModelsQuerys(User)
        user = orm.find_by_query(query_user)

        if not user:
            exception(
                "User does not exists",
                {"uui": uuid},
                409
            )

        orm.delete_by_query(query_user)

        return {
            "uuid": uuid
        }

    @classmethod
    def get_jobs(cls, **params):
        """
        Get user by any param
        """
        orm = ModelsQuerys(Job)
        jobs = orm.find_by_query(params)
        return list(map(lambda job: cls.__remove_unnecessary_fields(job), jobs))

    @classmethod
    def filter_job(cls, uuid: UUID):
        """
        Return job based on User skills experience
        """
        query_user = {
            "uuid": uuid
        }

        user_orm = ModelsQuerys(User)
        user = user_orm.find_by_query(query_user)

        if not user:
            exception(
                "User does not exists",
                {"uui": uuid},
                409
            )

        job_orm = ModelsQuerys(Job)
        jobs = job_orm.find_all()

        if not jobs:
            exception(
                "Job does not exists",
                {"uui": uuid},
                409
            )

        list_job = []
        for user_skills in user[0]["skills"]:
            for sk, xp in user_skills.items():
                for job in jobs:
                    validate_skill = [d for d in job["requiredSkills"] if sk in d and xp >= d[sk] * 0.5]
                    if validate_skill:

                        if "summary" not in job:
                            job["summary"] = {}

                        job["summary"]["matchedSkills"] = 1 if "matchedSkills" not in job["summary"] else job["summary"]["matchedSkills"] + 1
                        job["summary"]["reqSkills"] = len(job["requiredSkills"])
                        job["summary"]["yourSkills"] = sk if "yourSkills" not in job["summary"] else job["summary"]["yourSkills"] + ", " + sk

                        if job not in list_job:
                            job.pop("_id")
                            list_job.append(job)
        return list_job

    @staticmethod
    def __remove_unnecessary_fields(job: dict):
        job.__delitem__('_id')
        job.__delitem__('updated_at')
        job.__delitem__('created_at')
        return job

    @classmethod
    def create_job(cls, serializer: dict):
        """
        Create job
        """
        orm = ModelsQuerys(Job)

        query_job = {
            "companyName": serializer["companyName"],
            "positionName": serializer["positionName"],
        }

        job = orm.find_by_query(query_job)

        if job:
            exception(
                "job already exists",
                {
                    "companyName": serializer["companyName"],
                    "positionName": serializer["positionName"]
                },
                409
            )

        serializer["uuid"] = uuid4()
        orm.save(serializer)

        return {
            "uuid": serializer["uuid"],
            "companyName": serializer["companyName"],
            "positionName": serializer["positionName"]
        }

    @classmethod
    def update_job(cls, uuid: UUID, serializer: dict):
        """
        Update user
        """
        query_user = {
            "uuid": uuid
        }

        orm = ModelsQuerys(Job)
        job = orm.find_by_query(query_user)

        if not job:
            exception(
                "Job does not exists",
                {
                    "positionName": serializer["positionName"],
                    "companyName": serializer["companyName"]
                },
                409
            )

        serializer['updated_at'] = datetime.now()
        job = orm.update_by_query(query_user, serializer)

        return {
            "uuid_reference": uuid,
            "updated": job
        }

    @classmethod
    def delete_job(cls, uuid: UUID):
        """
        Delete user
        """
        query_jobs = {
            "uuid": uuid
        }

        orm = ModelsQuerys(Job)
        job = orm.find_by_query(query_jobs)

        if not job:
            exception(
                "Job does not exists",
                {"uui": uuid},
                409
            )

        orm.delete_by_query(query_jobs)

        return {
            "uuid": uuid
        }
