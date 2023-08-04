from datetime import datetime
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from tgbot.keyboards import inline
from tgbot.models.Enums import University
from tgbot.services.database import Database


class ProfileCreationForm(StatesGroup):
    nickname = State()
    description = State()
    photo_id = State()


async def create_profile(call: CallbackQuery):
    await call.answer("Loading...")
    await call.message.answer("What's your name?")
    await ProfileCreationForm.nickname.set()


async def set_nickname(message: Message, state: FSMContext):
    if len(message.text) > 255:
        return

    async with state.proxy() as data:
        data['nickname'] = message.text

    await message.answer("Tell us about you. This text will be shown for others")
    await ProfileCreationForm.next()


async def set_description(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await message.answer("Send us a photo")
    await ProfileCreationForm.next()


async def set_profile_photo(message: Message, state: FSMContext):
    try:
        file_id = message.photo.pop().file_id
    except Exception as e:
        print(e)
        return await message.answer("Please, send photo for your profile picture to continue.")

    db: Database = message.bot['config'].db
    async with state.proxy() as data:
        data["photo_id"] = file_id
        db.profiles_table.add_profile(message.from_id, data['nickname'], data['description'],
                                      data['photo_id'], True, datetime.now(), datetime.now())

    await state.finish()
    await message.answer("Done")
    print(db.profiles_table.print_all())


def profile_commands(dp: Dispatcher):
    dp.register_callback_query_handler(create_profile, callback_data="create_profile")
    dp.register_message_handler(set_nickname, state=ProfileCreationForm.nickname)
    dp.register_message_handler(set_description, state=ProfileCreationForm.description)
    dp.register_message_handler(set_profile_photo, state=ProfileCreationForm.photo_id, content_types=ContentType.PHOTO)
