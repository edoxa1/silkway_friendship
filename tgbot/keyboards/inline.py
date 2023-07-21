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
