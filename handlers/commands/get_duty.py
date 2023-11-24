from aiogram import types

from filters.auth import isuser
from loader import dp
from utils import duty


@dp.message_handler(isuser, commands=["getduty"])
async def send_duty(message: types.Message):
    await message.answer_chat_action(action='typing')
    await message.reply(duty.get(), parse_mode='Markdown')