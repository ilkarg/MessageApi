import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token = '20090319ead8fb22e003be97bda3e659c2e3f88a46881b0e987717bc5f0b95f7972a71077dbd921da5738')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    status = vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})
    return status

for event in longpoll.listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            id = event.user_id

            if msg == 'привет':
                res = sender(567096304, 'Привет!')
                print(res)
            else:
                res = sender(104690258, 'Я тебя не пойму')
                print(res)
    except Exception as err:
        print(err)