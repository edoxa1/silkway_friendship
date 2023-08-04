import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery


async def admin_start(message: Message):
    await message.reply("Hello, admin!")
    await message.answer_dice()


async def get_database_count(message: Message):
    db = message.bot['config'].db
    count = db.get_count()
    await message.answer(text=f"Total users: {count}")


async def callback_receiver(call: CallbackQuery):
    logging.info(f"Received callback data from {call.from_user.id}; data: {call.data}")
    await call.answer(f"Data is: {call.data}")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(get_database_count, commands=['count'], is_admin=True)
    dp.register_callback_query_handler(callback_receiver, is_admin=True)




