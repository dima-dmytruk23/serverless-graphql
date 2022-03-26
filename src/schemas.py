import random
import string
import uuid

import pydantic
import graphene

from graphene_pydantic import PydanticObjectType


class TodoModel(pydantic.BaseModel):
    object_id: uuid.UUID
    title: str
    description: str


class Todo(PydanticObjectType):
    class Meta:
        model = TodoModel


class TodoQuery(graphene.ObjectType):
    list_todos = graphene.List(Todo)

    def resolve_list_todos(self, info):
        """Resolver that creates a tree of Pydantic objects"""
        # TODO: get data from db
        return [
            TodoModel(
                object_id=uuid.uuid4(),
                title="".join(random.choice(string.ascii_letters) for _ in range(20)),
                description="".join(random.choice(string.ascii_letters) for _ in range(100))
            ) for _ in range(3)
        ]


todo_schema = graphene.Schema(query=TodoQuery)
