from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter


f_group = ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP])
