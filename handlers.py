from main import bot, dp
from keyboards import keyboard
from aiogram import types
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Тестируем WebApp!',
                           reply_markup=keyboard)

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message ):
    print(web_app_message.web_app_data.data)

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!')
