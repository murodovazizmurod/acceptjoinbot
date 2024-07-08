from aiogram import executor

from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
	pass
while True:
    try:
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    except Exception as e:
        bot.send_message(756639030, f"{e}")
        
