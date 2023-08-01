from aiogram import Dispatcher

from tgbot.handlers.user.register_user import register_user


def register_message_handlers(dp: Dispatcher):
    register_user(dp)
