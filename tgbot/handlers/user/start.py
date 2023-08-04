from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from tgbot.handlers.user.profile import profile_commands
from tgbot.keyboards import inline
from tgbot.models.Enums import University
from tgbot.services.database import Database, UsersTable


async def user_start(message: Message):
    await message.reply(f"Hello, {message.from_user.first_name}!", reply_markup=inline.generate_startup_keyboard())


async def find_someone(call: CallbackQuery):
    await call.answer("Loading...")  # always answer to calls!
    db: Database = call.bot['config'].db  # access DB using bot['config'] (see tgbot/config.py)


async def my_profile(call: CallbackQuery):
    await call.answer("Loading...")
    db: Database = call.bot['config'].db
    profile = db.profiles_table.get_profile(call.from_user.id)
    if not profile:
        kb = inline.generate_profile_empty_keyboard()
        await call.message.answer(text="You don't have profile", reply_markup=kb)
        return

    kb = inline.generate_profile_keyboard()
    text = profile.generate_text()
    await call.message.answer_photo(photo=profile.photo_id, caption=text, reply_markup=kb)


def register_user(dp: Dispatcher):
    # start command
    dp.register_message_handler(user_start, commands=["start"], state="*")
    # start menu callback handlers
    dp.register_callback_query_handler(find_someone, callback_data="find_someone")
    dp.register_callback_query_handler(my_profile, callback_data="my_profile")

    profile_commands(dp)
