from aiogram import types
from aiogram.dispatcher.filters import Filter
from sqlalchemy import select

from sqlalchemy.orm import Session

from utils.db.models import User
from loader import db_engine


session = Session(db_engine)


class IsUser(Filter):
    key = "is_user"
    db_req = select(User.id)

    async def check(self, message: types.Message):
        return message.from_user.id in list(session.scalars(self.db_req))


class IsAdmin(Filter):
    key = "is_admin"
    db_req = select(User.id).where(User.role.__eq__('admin'))

    async def check(self, message: types.Message):
        return message.from_user.id in list(session.scalars(self.db_req))


isadmin = IsAdmin()
isuser = IsUser()