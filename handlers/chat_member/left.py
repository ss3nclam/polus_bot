import logging

from aiogram import types

from filters.chat_type import isgroup
from loader import db_session, dp
from utils.db.models import User


@dp.message_handler(isgroup, content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def hello_new_user(message: types.Message):
    left_user = message.left_chat_member
    try:
        left_user = db_session.get(User, left_user.id)
        db_session.delete( left_user)
        db_session.commit()
        logging.info('Deleting left user from database: %s', 'successfully deleted')
    except Exception as error:
        logging.warning('Deleting left user from database problem: %s', error)