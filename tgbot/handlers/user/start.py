from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from tgbot.keyboards import inline
from tgbot.models.Enums import University


async def user_start(message: Message):
    await message.reply("Hello, user!", reply_markup=inline.generate_startup_keyboard())


async def find_someone(call: CallbackQuery):
    await call.message.answer(call.data)
    db = call.bot['config'].db  # access DB using bot['config'] (see tgbot/config.py)
    db.add_user(call.from_user.id, call.from_user.username, "abebus", University.AITU)
    await call.message.answer(f"Successfully registered {call.from_user.username}")
    user_tuple = db.get_user(call.from_user.id)
    await call.message.answer(user_tuple)
    await call.message.answer(f"Person id {call.from_user.id} exists: {db.user_exists(call.from_user.id)}")
    await call.message.answer(f"Person id 0 exists: {db.user_exists(0)}")
    # see tgbot/services/database.py to check all methods


async def my_profile(call: CallbackQuery):
    await call.message.answer(call.data)
    await call.answer("you chose tshirts")
    db = call.bot['config'].db
    db.print_all()

