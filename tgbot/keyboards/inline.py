from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_test_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(text="T-shirts", callback_data="shirts"),
           InlineKeyboardButton(text="Shoes", callback_data="shoes"))

    return kb


