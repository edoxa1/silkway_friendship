from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards import inline


async def user_start(message: Message):
    await message.reply("Hello, user!", reply_markup=inline.generate_startup_keyboard())

async def dicer(message: Message):
    answer_dice = await message.answer_dice()
    await message.answer(text=f"{answer_dice.dice.value}", reply_markup=inline.generate_test_keyboard())

async def find_someone(call: CallbackQuery):
    await call.message.answer(call.data)
    await call.answer("you chose shoes")

async def my_profile(call:CallbackQuery):
    await call.message.answer(call.data)
    await call.answer("you chose tshirts")

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(dicer, commands=["roll"])
    dp.register_callback_query_handler(find_someone, callback_data="find_someone")
    dp.register_callback_query_handler(my_profile, callback_data="my_profile")



