from src.nested_schemas import category_schema
from src.schemas import todo_schema


class Todo:
    @staticmethod
    def list(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def retrieve(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def filter(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def create(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def update(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def delete(query: str):
        result = todo_schema.execute(query)
        return result

    @staticmethod
    def nested_list_categories(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def nested_list_tags(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def create_category_nested(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def update_category_nested(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def create_tag_nested(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def update_tag_nested(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def bulk_create_tag_nested(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def bulk_update_tag_nested(query: str):
        result = category_schema.execute(query)
        return result

    @staticmethod
    def bulk_create_category_nested(query: str):
        result = category_schema.execute(query)
        print(result.errors)
        return result

    @staticmethod
    def bulk_update_category_nested(query: str):
        result = category_schema.execute(query)
        return result


list_todos = Todo.list
create_todo = Todo.create
retrieve_todo = Todo.retrieve
filter_todos = Todo.filter
update_todo = Todo.update
delete_todo = Todo.delete

nested_list_categories = Todo.nested_list_categories
nested_list_tags = Todo.nested_list_tags
create_category_nested = Todo.create_category_nested
update_category_nested = Todo.update_category_nested
create_tag_nested = Todo.create_tag_nested
update_tag_nested = Todo.update_tag_nested
bulk_create_tag_nested = Todo.bulk_create_tag_nested
bulk_update_tag_nested = Todo.bulk_update_tag_nested
bulk_create_category_nested = Todo.bulk_create_category_nested
bulk_update_category_nested = Todo.bulk_update_category_nested
