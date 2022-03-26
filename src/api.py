from src.schemas import todo_schema


class Todo:
    @staticmethod
    def list(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def create(query: str):
        ...


list_todos = Todo.list
create_todo = Todo.create
