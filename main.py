import logging

from aiogram import Bot, Dispatcher, bot, dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import asyncio

from config import *
from keyboards import *
import texts 


#API ='8055154686:AAF_YndX1nuHdGOKyq5-6WNb-ZwGQQ6UYa4'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(texts.start, reply_markup=start_kb)

@dp.message_handler(text = 'О нас' )
async def price(message: types.Message):
    await message.answer(texts.about, reply_markup=start_kb)

@dp.message_handler(text = 'Стоимость' )
async def info(message: types.Message):
    await message.answer("что вас интересует?", reply_markup=catalog_kb)

@dp.callback_query_handler(text='medium')
async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='big')
async def buy_l(call):
    await call.message.answer(texts.Lgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    await call.message.answer(texts.XLgame, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other, reply_markup=buy_kb)
    await call.answer()






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)