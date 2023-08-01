import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.filters.callback import CallbackFilter
from tgbot.handlers.register import register_message_handlers
from tgbot.middlewares.environment import EnvironmentMiddleware
from tgbot.misc.set_bot_commands import set_default_commands

logger = logging.getLogger(__name__)


def register_all_middlewares(dp: Dispatcher, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(CallbackFilter)


def register_all_handlers(dp: Dispatcher):
    register_message_handlers(dp)


async def on_startup(dp: Dispatcher, config):
    await set_default_commands(dp)  # set default commands. Use ctrl+LMB to set bot commands
    for uid in config.tg_bot.admin_ids:
        await dp.bot.send_message(uid, text="Бот запущен")


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    config = load_config("./tgbot/services/database.db", ".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    logger.info(f"Starting bot [@{(await bot.get_me()).username}].")
    await on_startup(dp, config)
    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await (await bot.get_session()).close()  # what the fuck


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
