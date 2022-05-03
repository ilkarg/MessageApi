import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='1073937415:AAE-hXKpOwjbom_C5T3wcncP6u5bhS4CXU0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    markup_btn1 = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Подписаться на рассылку', request_contact=True))
    await bot.send_message(message.chat.id, 'Для начала работы надо подписаться на рассылку', reply_markup=markup_btn1)

@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        print(message.from_user.id)
        await bot.send_message(message.chat.id, 'Вы успешно подписались на рассылку', reply_markup=keyboard2)
        phonenumber = str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        print(f'id - {message.contact.user_id}; phone_number - {message.contact.phone_number}')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)