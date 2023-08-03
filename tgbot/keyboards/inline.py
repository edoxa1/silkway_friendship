from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_test_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="T-shirts", callback_data="cringe"),
           InlineKeyboardButton(text="Shoes", callback_data="shoes"))

    return kb


def generate_startup_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="find someone", callback_data="find_someone"), 
           InlineKeyboardButton(text="my profile", callback_data="my_profile"))
    
    return kb


def generate_find_someone_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(InlineKeyboardButton(text="next", callback_data="next"),
           InlineKeyboardButton(text="match", callback_data="match"),
           InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu"))
    
    return kb


def generate_profile_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(InlineKeyboardButton(text="Deactivate", callback_data="deactivate"),
           InlineKeyboardButton(text="Edit profile", callback_data="edit_profile"),
           InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu"))
    
    return kb


def generate_match_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=3)
    # show @user or smth idk what to do with this
    return kb


def generate_deactivate_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="yes", callback_data="deactivate"),
           InlineKeyboardButton(text="no", callback_data="back_to_menu"))
    return kb


def generate_edit_profile_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(InlineKeyboardButton(text="Change profile picture", callback_data="change_profile_picture"),
           InlineKeyboardButton(text="Change profile bio", callback_data="change_profile_bio"),
           InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu"))
    
    return kb
