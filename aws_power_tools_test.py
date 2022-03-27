from typing import Dict

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import AppSyncResolver
from aws_lambda_powertools.logging.correlation_paths import APPSYNC_RESOLVER
from aws_lambda_powertools.utilities.typing import LambdaContext

from src.resolvers import router


tracer = Tracer()
logger = Logger()
app = AppSyncResolver()
app.include_router(router)


@tracer.capture_lambda_handler
@logger.inject_lambda_context(correlation_id_path=APPSYNC_RESOLVER)
def lambda_handler(event: Dict, context: LambdaContext):
    app.resolve(event, context)


if __name__ == '__main__':
    list_query = """
            query {
              listTodos {
                title
              }
            }
        """
    lambda_handler({"queryStringParameters": {"query": list_query}}, None)