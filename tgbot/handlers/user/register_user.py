from aiogram import Dispatcher

from tgbot.handlers.user import start


def register_user(dp: Dispatcher):
    dp.register_message_handler(start.user_start, commands=["start"], state="*")
    dp.register_message_handler(dicer.dicer, commands=["roll"])
    dp.register_callback_query_handler(start.find_someone, callback_data="find_someone")
    dp.register_callback_query_handler(start.my_profile, callback_data="my_profile")
