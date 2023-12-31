from aiogram import Dispatcher

from tgbot.handlers.user.start import register_user
from tgbot.handlers.admin.admin import register_admin


def register_message_handlers(dp: Dispatcher):
    register_user(dp)
    register_admin(dp)
