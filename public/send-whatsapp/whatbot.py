import pywhatkit
import keyboard
import sys
import mouse
from mysql.connector import connect, Error

def send_message(mobile, message_id, tab_close):
    message = ''
    status = True

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
    except Error as err:
        status = False
        print(err)

    if status:
        pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message, tab_close=tab_close)

def main():
    if len(sys.argv) >= 3:
        send_message(sys.argv[1], sys.argv[2], True)

if __name__ == '__main__':
    try:
        main()
        mouse.move(mouse.get_position()[0] - 50, mouse.get_position()[1] - 100)
        mouse.click(button='left')
        keyboard.press('enter')
    except Exception as err:
        print(err)