import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from mysql.connector import connect, Error
import sys

vk_session = vk_api.VkApi(token = '20090319ead8fb22e003be97bda3e659c2e3f88a46881b0e987717bc5f0b95f7972a71077dbd921da5738')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Подписаться на рассылку', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Отписаться от рассылки', color=VkKeyboardColor.NEGATIVE)

def sender(id, text, keyboard_ = None):
    if keyboard_ == None:
        status = vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})
    elif not keyboard_ == None and text == None:
        status = vk_session.method('messages.send', {'user_id': id, 'message': 'Выберите одно действие из предложенных', 'keyboard': keyboard_.get_keyboard(), 'random_id': 0})
    elif not keyboard_ == None and not text == None:
        status = vk_session.method('messages.send', {'user_id': id, 'message': text, 'keyboard': keyboard_.get_keyboard(), 'random_id': 0})
    
    return status

for event in longpoll.listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            id = event.user_id

            if msg == 'начать':
                sender(id, None, keyboard)
            elif msg == 'подписаться на рассылку':
                status = True

                try:
                    with connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='api_sender_db'
                    ) as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(f"INSERT INTO user_list (account_id, number_phone, messenger) VALUES ('{id}', 'NULL', 'vkontakte')")
                            connection.commit()
                except Error as error:
                    status = False
                    print(f'ERROR > {error}')

                if status:
                    sender(id, 'Вы успешно подписались на рассылку!', keyboard)
                else:
                    sender(id, 'Во время подписки на рассылку, что-то пошло не так, обратитесь за помощью к администратору', keyboard)
            elif msg.lower() == 'отписаться от рассылки':
                status = True
                
                try:
                    with connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='api_sender_db'
                    ) as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(f"DELETE FROM user_list WHERE account_id='{id}' AND messenger='vkontakte'")
                            connection.commit()
                except Error as error:
                    status = False
                    print(f'ERROR > {error}')

                if status:
                    sender(id, 'Вы успешно отписались от рассылки!', keyboard)
                else:
                    sender(id, 'Во время отписки от рассылки, что-то пошло не так, обратитесь за помощью к администратору', keyboard)
            else:
                sender(id, 'Я вас не понимаю :/\n1) Отправьте мне сообщение "Начать"\n2) Выберите одно действие из предложенных кликнув по нужной вам кнопке')
    except Exception as error:
        print(f'ERROR > {error}')