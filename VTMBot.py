import random

from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# 1. вітаємося і пропонуємо юзеру дії: кинути кубики або прочитати про клан інфу....
# робимо це через меню команд бота
# команди:  clans_info   roll_dice
@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Hello, vampire! \nChose an action in menu.')


# 2.1. якщо обрав кубики, то запитуємо к-сть наявних кубиків чорних та червоних та чи є додаткові
# @bot.message_handler(commands=['roll_dice'])
# def count_dices(message):
#     bot.send_message(message.chat.id, 'How many black cubes do you have?')
#     bot.register_next_step_handler(message, quantity_main)  #записуємо к-сть основних чорних кубиків

# def quantity_main(message):
#     bot.send_message(message.chat.id, 'How many red cubes do you have?')
#     bot.register_next_step_handler(message, quantity_red)  #записуємо к-сть червоних кубиків

# def quantity_red(message):
#     bot.send_message(message.chat.id, 'How many additional cubes do you have?')
#     bot.register_next_step_handler(message, quantity_additional)  #записуємо к-сть додаткових чорних кубиків

# def quantity_additional(message):
#     # взяти введену інфу про к-сть і перетворити в int. (передбачити можливе введення кількості текстом)
#     main_cubes = ?
#     additional_cubes = ?
#     return sum(main_cubes, additional_cubes)


# після введених данних про кількість і їх перетворення в int для зручності читання робимо змінні black та red
# black - кількість чорних кубиків, red - червоних
def black_cubes(black):
    return [random.randint(1, 10) for x in range(black)]

def red_cubes(red):
    return [random.randint(1, 10) for x in range(red)]


# 2.2. якщо хоче інфу про клани, то видаємо кнопки з назвами кланів
# @bot.message_handler(commands=['clans_info']):
#
# .......................

@app.route('/', methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot 02-12-2022", 200

#@app.route('/' + TOKEN, methods=['POST'])


# @app.route('/')
# def main():
#     bot.remove_webhook()
#     bot.set_webhook(url='unexpected-alysia-mariagodlevska.koyeb.app/' + TOKEN)
#     return 'Python Telegram Bot', 200


# if __name__ == '__VTMBot__':
#     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
#

