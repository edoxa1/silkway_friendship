from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from tgbot.keyboards import inline
from tgbot.models.Enums import University


async def user_start(message: Message):
    await message.reply(f"Hello, {message.from_user.first_name}!", reply_markup=inline.generate_startup_keyboard())


async def find_someone(call: CallbackQuery):
    db = call.bot['config'].db  # access DB using bot['config'] (see tgbot/config.py)
    if not db.user_exists(call.from_user.id):
        user = db.add_user(call.from_user.id, University.AITU)
        await call.message.answer(user.info())
        return

    await call.message.answer(f"Person id {call.from_user.id} exists: {db.user_exists(call.from_user.id)}")
    user = db.get_user(call.from_user.id)
    await call.message.answer(user.info())
    # see tgbot/services/database.py to check all methods


async def my_profile(call: CallbackQuery):
    await call.message.answer(call.data)
    await call.answer("you chose tshirts")
    db = call.bot['config'].db
    db.print_all()
    code = db.get_user_verification_code(call.from_user.id)
    if code:
        await call.message.answer(text=code)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(find_someone, callback_data="find_someone")
    dp.register_callback_query_handler(my_profile, callback_data="my_profile")

