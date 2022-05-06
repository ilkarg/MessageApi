import logging
from aiogram import Bot, Dispatcher, executor, types
from mysql.connector import connect, Error
import asyncio
import sys

bot = Bot(token='1073937415:AAE-hXKpOwjbom_C5T3wcncP6u5bhS4CXU0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def send_message(id, message_id):
    message = ''
    status = True

    print('Telegram_Bot > send_message')

    try:
        with connect(
            host='localhost',
            user='root',
            password='',
            database='api_sender_db'
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT message FROM message_list WHERE id=' + message_id)
                result = cursor.fetchall()
                message = result[0][0]
    except Error as error:
        status = False
        print(f'ERROR > {error}')

    if status:
        print(f'Telegram_Bot > Прочитал с БД - id: {id}; message: {message}')
        await bot.send_message(id, message if len(message.strip()) > 0 else 'Пустое сообщение')

async def main():
    if len(sys.argv) >= 3:
        id = None
        status = True
        print('Telegram_Bot > Начинаю работу...')

        try:
            with connect(
                host='localhost',
                user='root',
                password='',
                database='api_sender_db'
            ) as connection:
                with connection.cursor() as cursor:
                    print(f"Telegram_Bot > QUERY: SELECT account_id FROM user_list WHERE number_phone='{sys.argv[1]}'")
                    cursor.execute(f"SELECT account_id FROM user_list WHERE number_phone='{sys.argv[1]}'")
                    result = cursor.fetchall()
                    id = result[0][0]
                    print(f'Telegram_Bot > id = {id}')
        except Error as error:
            status = False
            print(f'ERROR > {error}')
        
        print(f'Telegram_Bot > status = {status}')

        if status and not id == None:
            print(f'Telegram_Bot > Прочитал с БД - id: {id}')
            await send_message(id, sys.argv[2])

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as error:
        print(f'ERROR > {error}')