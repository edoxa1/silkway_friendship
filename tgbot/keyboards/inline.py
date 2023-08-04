from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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


def generate_profile_keyboard(is_active: bool) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="Deactivate" if is_active else "Activate",
                                callback_data="deactivate" if is_active else "activate"),
           InlineKeyboardButton(text="Edit profile", callback_data="edit_profile"),
           InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu"))
    
    return kb


def generate_profile_empty_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(InlineKeyboardButton(text="Create profile", callback_data="create_profile"),
           InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu"))

    return kb


def generate_match_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=3)
    # show @user or smth idk what to do with this
    return kb


def generate_edit_profile_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="Name", callback_data="change_profile_name"),
           InlineKeyboardButton(text="Picture", callback_data="change_profile_picture"),
           InlineKeyboardButton(text="Bio", callback_data="change_profile_bio"))
    kb.add(InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu"))
    
    return kb
