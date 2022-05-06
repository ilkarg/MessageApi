import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from mysql.connector import connect, Error
import sys

def get_message(message_id):
    message = None
    status = True

    try:
        with connect(
            host='localhost',
            user='root',
            password='',
            database='api_sender_db'
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT message FROM message_list WHERE id={message_id}")
                result = cursor.fetchall()
                message = result[0][0]
    except Error as error:
        status = False
        print(f'ERROR > {error}')

    return message if len(message.strip()) > 0 and not message == None and status else None

def get_user_id(number_phone):
    id = None
    status = True

    try:
        with connect(
            host='localhost',
            user='root',
            password='',
            database='api_sender_db'
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT account_id FROM user_list WHERE number_phone='{number_phone}' AND messenger='vkontakte'")
                result = cursor.fetchall()
                id = result[0][0]
    except Error as error:
        status = False
        print(f'ERROR > {error}')

    return id if not id == None and status else None

def main():
    id = None
    message = None

    if len(sys.argv) >= 3:
        id = get_user_id(sys.argv[1])
        message = get_message(sys.argv[2])

        if not id == None and not message == None:
            vk_session = vk_api.VkApi(token = '20090319ead8fb22e003be97bda3e659c2e3f88a46881b0e987717bc5f0b95f7972a71077dbd921da5738')
            session_api = vk_session.get_api()
            longpoll = VkLongPoll(vk_session)
            vk_session.method('messages.send', {'user_id': id, 'message': message, 'random_id': 0})
            exit()

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'ERROR > {error}')