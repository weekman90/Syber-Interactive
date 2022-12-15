import telebot
from telebot import types

bot = telebot.TeleBot('5947646190:AAGY1OjktMtNzY0LvdKiArJbppoR3gRbXgY')


@bot.message_handler(commands=['start'])

def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Вход в систему')
    item2 = types.KeyboardButton('Выход')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=markup)


@bot.message_handler(content_types=['text'])

def autorization(message):

    if message.text == 'Вход в систему':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        exit = types.KeyboardButton('Выход')
        markup.add(exit)
        sent = bot.send_message(message.chat.id, 'Введите ключ для входа в систему',  reply_markup=markup)
        bot.register_next_step_handler(sent, login)

def login(message):

        if message.text == 'vD~8dA5W#OOSA%?':
            exit = types.KeyboardButton('Выход')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(exit)
            bot.send_message(message.chat.id, 'Вход успешен')
            hello = bot.send_message(message.chat.id, "Я калькулятор, что посчитаем?...", reply_markup=markup)
            bot.register_next_step_handler(hello, handle_text)

        elif message.text == "/start" or message.text == "Выход":
            sent=bot.send_message(message.chat.id, 'Начнём сначала')
            bot.register_next_step_handler(sent, autorization)
            return welcome(message)

        else:
            bot.send_message(message.chat.id, 'Пароль неверен')
            exit = types.KeyboardButton('Выход')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(exit)
            sent = bot.send_message(message.chat.id, 'Введите ключ для входа в систему', reply_markup=markup)
            bot.register_next_step_handler(sent, login)



@bot.message_handler(content_types=['text'])

def handle_text(message):

    if message.text == "/start" or message.text == "Выход":
        sent=bot.send_message(message.chat.id, 'Начнём сначала')
        bot.register_next_step_handler(sent, autorization)
        return welcome(message)

    exit = types.KeyboardButton('Выход')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(exit)
    bot.send_message(message.chat.id, f'Получится вот столько: {eval(message.text)}')
    hello = bot.send_message(message.chat.id, "Хорошо, что посчитаем ещё?...", reply_markup=markup)
    bot.register_next_step_handler(hello,handle_text)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)







