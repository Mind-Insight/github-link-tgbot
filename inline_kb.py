from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

inline_btn = InlineKeyboardButton('GitHub', url='https://github.com/Mind-Insight')
ikb = InlineKeyboardMarkup(row_width=2).add(inline_btn)