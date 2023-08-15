from aiogram import executor

from init import dp, app_verbose
from handlers import echo, start


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
