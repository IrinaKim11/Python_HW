from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor, callback_data

from Seminar_10.keyboards.inline.choice_buttons import choice
from config import *
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
import random
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(Command("start"))
async def choice_sign(message: Message):
    await message.answer(text="Привет! Этот бот ответит на твой вопрос или просто придаст уверенности в себе.😉\n"
                              "Задай вопрос и нажми кнопку 'Ответ'!\n"
                        "Или нажми 'Мотивация', чтобы получить заряд позитива!",
                         reply_markup=choice)


@dp.callback_query_handler(text='start')
async def make_answer(call: CallbackQuery):
    lst_answ = ["да", "духи говорят нет", "возможно", "спроси позже", "не сейчас", "не могу сказать", "есть сомнения", "очень вероятно", "шансов немного", "точно нет", "определенно"]
    await call.answer(random.choice(lst_answ), show_alert=True)

@dp.callback_query_handler(text='mot')
async def make_answer(call: CallbackQuery):
    lst_answ = ["Ты молодец!", "Все возможно!", "У тебя получится!", "Лучший!", "Нормально делай, нормально будет!", "У тебя гениальный ум!", "Ты потрясающая личность!", "Будь собой!", "У тебя классные шутки!"]
    await call.answer(random.choice(lst_answ), show_alert=True)


executor.start_polling(dp)