import telebot

bot = telebot.TeleBot('1073937415:AAE-hXKpOwjbom_C5T3wcncP6u5bhS4CXU0')

def send_messages(id_list, message):
    if (isinstance(id_list, list)):
        for id in id_list:
            try:
                bot.send_message(id, message)
                print(f'Сообщение: [{message}] доставлено пользователю - {id}')
            except Exception as error:
                print(f'ОШИБКА: {error}')
    else:
        try:
            bot.send_message(id_list, message)
            print(f'Сообщение: [{message}] доставлено пользователю - {id_list}')
        except Exception as error:
            print(f'ОШИБКА: {error}')

send_messages([772238966, 1, 772238966], 'Я запустился!') # отправка нескольким пользователям
send_messages(772238966, 'Я родился!') # отправка одному пользователю

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        print('Сообщение от: ' + str(message.from_user.id))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
        print('Сообщение от: ' + str(message.from_user.id))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        print('Сообщение от: ' + str(message.from_user.id))

bot.polling(none_stop=True, interval=0)