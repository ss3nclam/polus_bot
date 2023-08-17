from aiogram import types

from loader import dp
from filters.group import f_group
from utils import duty


@dp.message_handler(f_group, commands=["get_duty"])
async def send_duty(message: types.Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action='typing')
    duty_person = duty.today()
    text = f'*Дежурный: ❗️*\n   {duty_person}' if duty_person else '*График дежурств еще не заполнен* 🤷‍♂️'
    await message.reply(text, parse_mode='Markdown')