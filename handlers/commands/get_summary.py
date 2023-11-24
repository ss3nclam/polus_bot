from aiogram import types

from filters.auth import isuser
from loader import dp
from utils import summary


@dp.message_handler(isuser, commands=["getsummary"])
async def send_summary(message: types.Message):
    await message.answer_chat_action(action='typing')
    await message.reply(summary.get(), parse_mode='Markdown')