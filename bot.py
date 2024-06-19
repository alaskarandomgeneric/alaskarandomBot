from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os

TOKEN = os.getenv('YOUR_BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello World!")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
