from uuid import uuid4
from datetime import datetime
from app.core.exceptions import exception
from app.core.models import User
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
    def update_users(cls, uuid, serializer: dict):
        """
        Update user
        """
        query_user = {
            "uuid": uuid
        }

        orm = ModelsQuerys(User)
        user = orm.find_by_query(query_user)
        print(type(user))

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
    def delete_users(cls, uuid):
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