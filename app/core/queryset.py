from . import exceptions


class ModelsQuerys:
    """
    Querys of model using mongoengine
    """

    def __init__(self, model):
        self.model = model

    def save(self, data_to_save: dict):
        model = self.model(**data_to_save)
        doc = model.save()
        return doc

    def find_by_query(self, query: dict, as_pymongo=True):
        if as_pymongo:
            docs = self.model.objects(**query).as_pymongo()
            return docs
        else:
            docs = self.model.objects(**query)
            return docs

    def find_all(self, as_pymongo=True, to_json=False):
        if as_pymongo:
            docs = self.model.objects().as_pymongo()
            return docs
        if to_json:
            docs = self.model.objects().to_json()
            return docs
        else:
            docs = self.model.objects()
            return docs

    def delete_by_query(self, query: dict):
        docs = self.model.objects(**query).first()
        if not docs:
            exceptions.raise_not_found(
                str([str(i) for i in query.keys()]),
                str([str(i) for i in query.values()])
            )
        deleted = docs.delete()
        return deleted

    def update_by_query(self, query: dict, data_to_put: dict):
        docs = self.model.objects(**query).first()
        if not docs:
            exceptions.raise_not_found(
                str([str(i) for i in query.keys()]),
                str([str(i) for i in query.values()])
            )
        updated = docs.update(**data_to_put)
        return updated
