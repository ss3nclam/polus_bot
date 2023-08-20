from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter


isgroup = ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP])
isprivate = ChatTypeFilter(chat_type=[types.ChatType.PRIVATE])
