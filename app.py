from aiogram import executor

import handlers
from loader import dp
from utils import scheduler


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=scheduler.start())
