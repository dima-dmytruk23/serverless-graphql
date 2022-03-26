import json

from src.api import create_todo, list_todos


methods = {
    # Main methods
    "query": {"listTodos": list_todos},
    "mutation": {"createTodo": create_todo},
#     "query": {"retrieveTodo": retrieve_todo},
#     "mutation": {"updateTodo": update_todo},
#     "mutation": {"deleteTodo": delete_todo},
#
#     # Additional methods
#     "query": {"searchTodos": search_todos},
#     "query": {"filterTodos": filter_todos},
#     "query": {"filterTodos": ordering_todos},
}


def lambda_handler(event, context):
    query_string = event['queryStringParameters'].get('query')
    query_splitted = query_string.strip().split()

    query_type = query_splitted[0]
    if query_type not in methods:
        return {'statusCode': 405, 'body': {"Query type must by `query` or `mutation`"}}

    query_method = query_splitted[2]
    if query_method not in methods[query_type]:
        return {'statusCode': 405, 'body': {"API method not found"}}

    response = methods[query_type][query_method](query_string)

    return {'statusCode': 200, 'body': json.dumps(response.data)}


if __name__ == "__main__":
    query = """
        query {
          listTodos {
            title,
            description
          }
        }
    """
    response = lambda_handler({"queryStringParameters": {"query": query}}, None)
    print(response)
