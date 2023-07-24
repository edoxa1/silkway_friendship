from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards import inline


async def user_start(message: Message):
    await message.reply(f"Hello, {message.from_user.first_name}!", reply_markup=inline.generate_startup_keyboard())

async def dicer(message: Message):
    answer_dice = await message.answer_dice()
    await message.answer(text=f"{answer_dice.dice.value}", reply_markup=inline.generate_test_keyboard())

async def find_someone(call: CallbackQuery):
    await call.message.answer("finding someone...", reply_markup=inline.generate_find_someone_keyboard())
    await call.answer("you chose find someone")

async def my_profile(call:CallbackQuery):
    await call.message.answer("your profile:\n", reply_markup=inline.generate_profile_keyboard())
    await call.answer("you chose my profile")

async def deactivate(call:CallbackQuery):
    await call.message.answer("are you sure?", reply_markup=inline.generate_deactivate_keyboard())

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(dicer, commands=["roll"])
    dp.register_callback_query_handler(find_someone, callback_data="find_someone")
    dp.register_callback_query_handler(my_profile, callback_data="my_profile")
    dp.register_callback_query_handler(deactivate, callback_data="deactivate")




