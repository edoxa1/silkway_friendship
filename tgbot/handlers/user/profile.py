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
    file_id = message.photo.pop().file_id
    db: Database = message.bot['config'].db
    async with state.proxy() as data:
        data["photo_id"] = file_id
        db.profiles_table.add_profile(message.from_id, data['nickname'], data['description'],
                                      data['photo_id'], True, datetime.now(), datetime.now())

    await state.finish()
    await message.answer("Done")


async def reactivate_profile(call: CallbackQuery):
    db: Database = Database.get_instance()
    profile = db.profiles_table.get_profile(call.from_user.id)
    if not profile:
        await call.message.answer("Error")

    if profile.is_active:
        profile.deactivate()
        await call.answer("Deactivated")
    else:
        profile.activate()
        await call.answer("Activated")

    await call.message.delete()
    kb = inline.generate_profile_keyboard(profile.is_active)
    text = profile.generate_text()
    await call.message.answer_photo(photo=profile.photo_id, caption=text, reply_markup=kb)


async def edit_profile(call: CallbackQuery):
    await call.answer("Loading...")
    kb = inline.generate_edit_profile_keyboard()
    await call.message.answer("I want to change...", reply_markup=kb)
    await call.message.delete()


class ProfileEditForm(StatesGroup):
    name = State()
    description = State()
    photo = State()


async def edit_profile_name(call: CallbackQuery):
    await call.answer("Loading")
    await ProfileEditForm.name.set()
    await call.message.delete()
    await call.message.answer("Enter new name. Must be less than 255 symbols")


async def change_nickname(message: Message, state: FSMContext):
    if len(message.text) > 255:
        await message.answer("Too long name!")
        return

    await state.finish()
    db: Database = Database.get_instance()
    profile = db.profiles_table.get_profile(message.from_id)
    profile.change_nickname(message.text)

    text = f"Your new profile: \n{profile.generate_text()}"
    kb = inline.generate_profile_keyboard(profile.is_active)
    await message.answer_photo(photo=profile.photo_id, caption=text, reply_markup=kb)


async def edit_profile_picture(call: CallbackQuery):
    await call.answer("Loading")
    await ProfileEditForm.photo.set()
    await call.message.delete()
    await call.message.answer("Send us a new photo")


async def change_profile_photo(message: Message, state: FSMContext):
    file_id = message.photo.pop().file_id
    db: Database = Database.get_instance()
    profile = db.profiles_table.get_profile(message.from_id)
    profile.change_photo_id(file_id)

    text = f"Your new profile: \n{profile.generate_text()}"
    kb = inline.generate_profile_keyboard(profile.is_active)
    await message.answer_photo(photo=profile.photo_id, caption=text, reply_markup=kb)
    await state.finish()


async def edit_profile_bio(call: CallbackQuery):
    await call.answer("Loading")
    await ProfileEditForm.description.set()
    await call.message.delete()
    await call.message.answer("Send us a new bio")


async def change_profile_bio(message: Message, state: FSMContext):
    db: Database = Database.get_instance()
    profile = db.profiles_table.get_profile(message.from_id)
    profile.change_description(message.text)

    text = f"Your new profile: \n{profile.generate_text()}"
    kb = inline.generate_profile_keyboard(profile.is_active)
    await message.answer_photo(photo=profile.photo_id, caption=text, reply_markup=kb)
    await state.finish()


def profile_commands(dp: Dispatcher):
    # profile creation state machine
    dp.register_callback_query_handler(create_profile, callback_data="create_profile")
    dp.register_message_handler(set_nickname, state=ProfileCreationForm.nickname)
    dp.register_message_handler(set_description, state=ProfileCreationForm.description)
    dp.register_message_handler(set_profile_photo, state=ProfileCreationForm.photo_id, content_types=ContentType.PHOTO)
    # profile [de]activation
    dp.register_callback_query_handler(reactivate_profile, callback_data=["activate", "deactivate"])
    # edit profile
    dp.register_callback_query_handler(edit_profile, callback_data="edit_profile")
    dp.register_callback_query_handler(edit_profile_name, callback_data="change_profile_name")
    dp.register_message_handler(change_nickname, state=ProfileEditForm.name)
    dp.register_callback_query_handler(edit_profile_picture, callback_data="change_profile_picture")
    dp.register_message_handler(change_profile_photo, state=ProfileEditForm.photo, content_types=ContentType.PHOTO)
    dp.register_callback_query_handler(edit_profile_bio, callback_data="change_profile_bio")
    dp.register_message_handler(change_profile_bio, state=ProfileEditForm.description)
