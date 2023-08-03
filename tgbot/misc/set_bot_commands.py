from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScope, BotCommandScopeChat


async def set_default_commands(dp: Dispatcher):
    await set_user_commands(dp)
    await set_admin_commands(dp)


async def set_user_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        BotCommand("start", "Start bot"),
    ])


async def set_admin_commands(dp: Dispatcher):
    admins = dp.bot['config'].tg_bot.admin_ids
    for admin_id in admins:
        await dp.bot.set_my_commands([
            BotCommand("start", "Start bot"),
            BotCommand("verify", "verify user")],
            scope=BotCommandScopeChat(admin_id)
        )
