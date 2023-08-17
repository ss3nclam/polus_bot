from aiogram import types

from loader import dp
from filters.group import f_group


@dp.message_handler(f_group, commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")