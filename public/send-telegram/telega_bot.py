import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from mysql.connector import connect, Error

bot = Bot(token='1073937415:AAE-hXKpOwjbom_C5T3wcncP6u5bhS4CXU0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    markup_btn1 = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Подписаться на рассылку', request_contact=True))
    await bot.send_message(message.chat.id, 'Для начала работы надо подписаться на рассылку', reply_markup=markup_btn1)

@dp.message_handler(content_types=['contact'])
async def contact(message):
    status = False

    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        await bot.send_message(message.chat.id, 'Вы успешно подписались на рассылку', reply_markup=keyboard2)
        phonenumber = str(message.contact.phone_number)
        user_id = str(message.contact.user_id)

        try:
            with connect(
                host='localhost',
                user='root',
                password='',
                database='api_sender_db'
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO user_list (account_id, number_phone, messenger) VALUES ('{user_id}', '{phonenumber}', 'telegram')")
                    connection.commit()
        except Error as error:
            status = False
            print(f'ERROR > {error}')

        if status:
            print(f'id - {message.contact.user_id}; phone_number - {message.contact.phone_number}')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)