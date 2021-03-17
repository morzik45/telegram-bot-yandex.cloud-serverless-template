import logging

from aiogram import Dispatcher

from handlers.users import bot_help, start


async def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(bot_help, commands=["help"])

    logging.debug("Handlers are registered.")
