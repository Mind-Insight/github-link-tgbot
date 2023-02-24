from aiogram import Dispatcher, Bot, executor, types
from config import TOKEN
from inline_kb import ikb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_link(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text='https://github.com/Mind-Insight', reply_markup=ikb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)