from aiogram import types

from filters.auth import isuser
from loader import dp


@dp.message_handler(isuser, commands=["start"])
async def send_hello(message: types.Message, name=''):
    await message.answer(f"Hi{name}\!\nI\'m EchoBot\!\nPowered by aiogram\.", parse_mode='MarkdownV2')