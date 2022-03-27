from typing import List

import pydantic
import graphene

from graphene_pydantic import PydanticObjectType, PydanticInputObjectType
from pydantic import BaseModel


class TodoModel(pydantic.BaseModel):
    title: str
    description: str


class ListTodoModel(BaseModel):
    items: List[TodoModel]
    key: str


class UpdateTodoModel(pydantic.BaseModel):
    title: str
    description: str
    object_id: str


class Todo(PydanticObjectType):
    class Meta:
        model = TodoModel


class ListTodo(PydanticObjectType):
    class Meta:
        model = ListTodoModel


data = ListTodoModel(**{"items":
            [TodoModel(**{"title": "MZjSZHgfEdtQuPBosvas",
                          "description": "LRGWcNlxQOmWKCfKPxDDGvQbuolIdTwNIOOpVPSLVixLCeqwDleUKnyjFxgWDchnFvyIsNxseJuHZgKjnjSrchDLsyiaAwPSUKHt"}),
             TodoModel(**{"title": "NPNnOjONKwyisQknwuzh",
                          "description": "TnjCCllOAydsVhQNEhvCiWMKpnazOzThVyHNpLGSyjqMWtXvwEKMbTCHptqAdbPfRjiQRgdzmyuFSkyNZefnxrufXVxZFmLrypfU"}),
             TodoModel(**{"title": "FSsMjCYEPoIlrCEAulbK",
                          "description": "dzWLXZjvNKNThutPghYafNyiiKElPaXpFFMSjqgitGdEliWUQLgmMVpNcZYVdjUkmEvUErUbGdAXKeHKCdeIpqLqsBuLkjFjUpHG"})
             ],
        "key": "532525"
        })


class TodoInput(PydanticInputObjectType):
    class Meta:
        model = TodoModel


class Todo1Input(PydanticInputObjectType):
    class Meta:
        model = TodoModel
        exclude = ("description",)


class UpdateTodoInput(PydanticInputObjectType):
    class Meta:
        model = UpdateTodoModel


class CreateTodo(graphene.Mutation):
    class Arguments:
        todo = TodoInput()
        todo1 = Todo1Input()

    Output = Todo

    @staticmethod
    def mutate(parent, info, todo, todo1):
        todo_model = TodoModel(**todo)
        print(f"{todo_model=}, {todo1=}")
        # TODO: save to db
        return todo


class UpdateTodo(graphene.Mutation):
    class Arguments:
        todo = UpdateTodoInput()

    Output = Todo

    @staticmethod
    def mutate(parent, info, todo):
        update_model = UpdateTodoModel(**todo)
        print(f"{todo=}")
        # TODO: save to db
        return todo


class DeleteTodo(graphene.Mutation):
    class Arguments:
        object_id = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(parent, info, object_id):
        print(f"{object_id=}")
        # TODO: save to db
        ok = True
        return DeleteTodo(ok=ok)


class TodoQuery(graphene.ObjectType):
    list_todos = graphene.Field(ListTodo)
    retrieve_todo = graphene.Field(Todo, title=graphene.String(required=True))
    filter_todos = graphene.Field(ListTodo, title=graphene.String(), args={"description": graphene.String()})


class TodoMutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()


todo_schema = graphene.Schema(query=TodoQuery, mutation=TodoMutation)
