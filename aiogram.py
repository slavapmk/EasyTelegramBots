from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

bot = Bot(token='ТОКЕН')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Привет! Я async-бот.")

if __name__ == '__main__':
    executor.start_polling(dp)
