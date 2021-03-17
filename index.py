import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from webhook import WebhookRequestHandler
from handlers import register_handlers


logging.basicConfig(level=logging.INFO)

<<<<<<< HEAD
bot = Bot(token=os.environ.get("TG_TOKEN", 0), parse_mode="HTML", validate_token=False)
=======
bot = Bot(token=os.environ.get('TG_TOKEN', 0), parse_mode='HTML', validate_token=False)
>>>>>>> master
dp = Dispatcher(bot=bot)
dp.middleware.setup(LoggingMiddleware())


async def handler(event, context):
    """Yandex.Cloud functions handler."""
<<<<<<< HEAD
    if event.get("httpMethod") == "POST":
        token = event.get("params", {}).get("token")
=======
    if event.get("httpMethod") == 'POST':
        token = event.get('params', {}).get('token')
>>>>>>> master
        try:
            with dp.bot.with_token(token, validate_token=True):
                await register_handlers(dp=dp)
                return await WebhookRequestHandler(dp=dp).post(event)
        except Exception as e:
            logging.error(e)
<<<<<<< HEAD
        return {"statusCode": 200, "body": "ok"}
    return {"statusCode": 405}
=======
        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 405}
>>>>>>> master
