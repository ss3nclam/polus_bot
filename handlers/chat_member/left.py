import logging

from aiogram import types
from sqlalchemy.orm import Session

from filters.chat_type import isgroup
from loader import db_engine, dp
from utils.db.models import User


@dp.message_handler(isgroup, content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def hello_new_user(message: types.Message):
    await message.answer_chat_action(action='typing')
    left_user = message.left_chat_member
    try:
        session = Session(db_engine)
        left_user = session.get(User, left_user.id)
        session.delete( left_user)
        session.commit()
        logging.info('Deleting left user from database: %s', 'successfully deleted')
    except Exception as error:
        logging.warning('Deleting left user from database problem: %s', error)