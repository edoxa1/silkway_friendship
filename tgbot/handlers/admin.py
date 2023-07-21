import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards import inline


async def admin_start(message: Message):
    await message.reply("Hello, admin!", reply_markup=inline.generate_test_keyboard())
    await message.answer_dice()


async def callback_receiver(call: CallbackQuery):
    logging.info(f"Received callback data from {call.from_user.id}; data: {call.data}")
    await call.answer(f"Data is: {call.data}")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_callback_query_handler(callback_receiver, is_admin=True)




