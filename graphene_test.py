import json

from src.api import create_todo, list_todos, retrieve_todo, filter_todos, update_todo, delete_todo, \
    nested_list_categories, nested_list_tags, create_category_nested, update_category_nested, create_tag_nested, \
    update_tag_nested, bulk_create_tag_nested, bulk_update_tag_nested, bulk_create_category_nested, \
    bulk_update_category_nested

methods = {
    "query": {
        "listTodos": list_todos,
        "retrieveTodo": retrieve_todo,
        "filterTodos": filter_todos,

        "nestedListCategories": nested_list_categories,
        "nestedListTags": nested_list_tags,
    },
    "mutation": {
        "createTodo": create_todo,
        "updateTodo": update_todo,
        "deleteTodo": delete_todo,
        "createCategoryNested": create_category_nested,
        "updateCategoryNested": update_category_nested,
        "createTagNested": create_tag_nested,
        "updateTagNested": update_tag_nested,
        "bulkCreateTagNested": bulk_create_tag_nested,
        "bulkUpdateTagNested": bulk_update_tag_nested,
        "bulkCreateCategoryNested": bulk_create_category_nested,
        "bulkUpdateCategoryNested": bulk_update_category_nested,
    },
}


def lambda_handler(event, context):
    query_string = event['queryStringParameters'].get('query')
    query_splitted = query_string.strip().split()

    query_type = query_splitted[0]
    if query_type not in methods:
        return {'statusCode': 405, 'body': {"Query type must by `query` or `mutation`"}}

    query_method = query_splitted[2]
    if "(" in query_method:
        query_method = query_method.split("(")[0]
    if query_method not in methods[query_type]:
        return {'statusCode': 405, 'body': {"API method not found"}}

    response = methods[query_type][query_method](query_string)

    return {'statusCode': 200, 'body': json.dumps(response.data)}


if __name__ == "__main__":
    # 1. List with paginations
    list_query = """
        query {
          listTodos {
            items {
                description
            },
            key
          }
        }
    """
    list_response = lambda_handler({"queryStringParameters": {"query": list_query}}, None)
    print(f"{list_response=}")

    # 2. Retrieve
    retrieve_query = """
        query {
            retrieveTodo(title: "NPNnOjONKwyisQknwuzh") {
            title,
            description
        }
    }
    """
    retrieve_response = lambda_handler({"queryStringParameters": {"query": retrieve_query}}, None)
    print(f"{retrieve_response=}")

    # 3. Filters
    filter_query = """
        query {
            filterTodos(title: "NPNnOjONKwyisQknwuzh", description: "NPNnOjONKwyisQknwuzh") {
            items {
                description
            },
            key
        }
    }
    """
    filter_response = lambda_handler({"queryStringParameters": {"query": filter_query}}, None)
    print(f"{filter_response=}")

    # 4. Create
    create_query = """
        mutation {
            createTodo(todo: {
                title: "Jerry",
                description: "Smith"
            }, todo1: {
                title: "Jerry1"
            }) {
                title
            }
        }
    """
    create_response = lambda_handler({"queryStringParameters": {"query": create_query}}, None)
    print(f"{create_response=}")

    # 5. Update
    update_query = """
        mutation {
            updateTodo(todo: {
                objectId: "12412",
                title: "Jerry",
                description: "Smith"
            }) {
                title
            }
        }
    """
    update_response = lambda_handler({"queryStringParameters": {"query": update_query}}, None)
    print(f"{update_response=}")

    # 6. Delete
    delete_query = """
        mutation {
            deleteTodo(objectId: "12412") {
                ok
            }
        }
    """
    delete_response = lambda_handler({"queryStringParameters": {"query": delete_query}}, None)
    print(f"{delete_response=}")

    # 7. Nested list one-to-many
    nested_list_categories_query = """
        query {
          nestedListCategories {
            items {
                title,
                tags {
                    title
                }
            },
            key
          }
        }
    """
    nested_list_categories_response = lambda_handler({"queryStringParameters": {"query": nested_list_categories_query}}, None)
    print(f"{nested_list_categories_response=}")

    # 8. Nested list many-to-one
    nested_list_tags_query = """
        query {
          nestedListTags {
            items {
                title,
                category {
                    title
                }
            },
            key
          }
        }
    """
    nested_list_tags_response = lambda_handler({"queryStringParameters": {"query": nested_list_tags_query}}, None)
    print(f"{nested_list_tags_response=}")

    # 9. Nested create one-to-many
    nested_create_category_query = """
        mutation {
            createCategoryNested(category: {
                title: "Jerry",
                tags: [
                 {
                    title: "afasf"
                 }
                ]
            }) {
                title
            }
        }
    """
    nested_create_category_response = lambda_handler({"queryStringParameters": {"query": nested_create_category_query}}, None)
    print(f"{nested_create_category_response=}")

    # 10. Nested update one-to-many
    nested_update_category_query = """
            mutation {
                updateCategoryNested(category: {
                    title: "Jerry",
                    tags: [
                     {
                        title: "afasf"
                     }
                    ]
                }) {
                    title,
                    tags {
                        title
                    }
                }
            }
        """
    nested_update_category_response = lambda_handler({"queryStringParameters": {"query": nested_update_category_query}}, None)
    print(f"{nested_update_category_response=}")

    # 11. Nested create many-to-one
    nested_create_tag_query = """
        mutation {
            createTagNested(tag: {
                title: "Jerry",
                category: {
                    title: "afasf"
                 }
            }) {
                title,
                category {
                  title
                }
            }
        }
    """
    nested_create_tag_response = lambda_handler({"queryStringParameters": {"query": nested_create_tag_query}}, None)
    print(f"{nested_create_tag_response=}")

    # 12. Nested update one-to-many
    nested_update_tag_query = """
        mutation {
            updateTagNested(tag: {
                title: "Jerry",
                category: {
                    title: "afasf"
                 }
            }) {
                title,
                category {
                    title
                }
            }
        }
    """
    nested_update_tag_response = lambda_handler({"queryStringParameters": {"query": nested_update_tag_query}}, None)
    print(f"{nested_update_tag_response=}")

    # 13. Bulk create many-to-one
    nested_bulk_create_tag_query = """
        mutation {
            bulkCreateTagNested(tags: [{
                title: "Jerry",
                category: {
                    title: "afasf"
                 }
            }, {
                title: "Jerry1",
                category: {
                    title: "afasf"
                 }
            }]) {
                title,
                category {
                    title
                }
            }
        }
    """
    nested_bulk_create_tag_response = lambda_handler({"queryStringParameters": {"query": nested_bulk_create_tag_query}}, None)
    print(f"{nested_bulk_create_tag_response=}")

    # 14. Bulk update many-to-one
    nested_bulk_update_tag_query = """
            mutation {
            bulkUpdateTagNested(tags: [{
                title: "Jerry",
                category: {
                    title: "afasf"
                 }
            }, {
                title: "Jerry1",
                category: {
                    title: "afasf"
                 }
            }]) {
                title,
                category {
                    title
                }
            }
        }
    """
    nested_bulk_update_tag_response = lambda_handler({"queryStringParameters": {"query": nested_bulk_update_tag_query}}, None)
    print(f"{nested_bulk_update_tag_response=}")

    # 15. Bulk create one-to-many
    nested_bulk_create_category_query = """
        mutation {
            bulkCreateCategoryNested(categories: [
            {
                title: "Jerry",
                tags: [
                 {
                    title: "afasf"
                 },
                 {
                    title: "afasf1"
                 }
                ]
            },
            {
                title: "Jerry1",
                tags: [
                 {
                    title: "afasf"
                 }
                ]
            }]) {
                title,
                tags {
                    title
                }
            }
        }
    """
    nested_bulk_create_category_response = lambda_handler(
        {"queryStringParameters": {"query": nested_bulk_create_category_query}}, None)
    print(f"{nested_bulk_create_category_response=}")

    # 16. Bulk update many-to-one
    nested_bulk_update_category_query = """
        mutation {
            bulkUpdateCategoryNested(categories: [
            {
                title: "Jerry",
                tags: [
                 {
                    title: "afasf"
                 },
                 {
                    title: "afasf1"
                 }
                ]
            },
            {
                title: "Jerry1",
                tags: [
                 {
                    title: "afasf"
                 }
                ]
            }]) {
                title,
                tags {
                    title
                }
            }
        }
    """
    nested_bulk_update_category_response = lambda_handler({"queryStringParameters": {"query": nested_bulk_update_category_query}}, None)
    print(f"{nested_bulk_update_category_response=}")
