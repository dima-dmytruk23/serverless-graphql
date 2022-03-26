import asyncio

from aws_lambda_powertools.event_handler import AppSyncResolver


app = AppSyncResolver()


@app.resolver(field_name="createSomething")
async def create_something_async(*args):
    await asyncio.sleep(1)  # Do async stuff
    print(f"{args}")
    return "created this value"
