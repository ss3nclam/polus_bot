from aiogram import types

from filters.auth import isuser
from loader import dp
from utils import weather


@dp.message_handler(isuser, commands=["get_weather"])
async def send_weather(message: types.Message):
    await message.answer_chat_action(action='typing')
    await message.reply(weather.get(), parse_mode='Markdown')