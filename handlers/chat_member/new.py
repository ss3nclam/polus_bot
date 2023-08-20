import logging
from datetime import datetime

from aiogram import types
from sqlalchemy.orm import Session

from filters.chat_type import isgroup
from handlers.commands.start import send_hello
from loader import db_engine, dp
from utils.db.models import User


@dp.message_handler(isgroup, content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def hello_new_user(message: types.Message):
    await message.answer_chat_action(action='typing')
    new_users = message.new_chat_members
    new_users_names = ', ' + (', '.join(f'[{new_user.first_name}](tg://user?id={new_user.id})' for new_user in new_users))[::-1].replace(',', 'dna ', 1)[::-1]
    await send_hello(message, new_users_names)
    for new_user in new_users:
        try:
            with Session(db_engine) as session:
                new_user = User(id=new_user.id, name=new_user.first_name, created=datetime.now())
                session.add(new_user)
                session.commit()
                logging.info('New user to Database writing: %s', 'successfully writed')
        except Exception as error:
            logging.warning('New user to Database writing problem: %s', error)