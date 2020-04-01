import telebot
import pymorphy2
import config
import random
from telebot import types
from admin import admin

bot = telebot.TeleBot(config.TOKEN)
gen = 'Сгенерировал(а)'
kv = 'Квас начал(а)'
uv = 1
tb = telebot.TeleBot(config.TOKEN)
print('Бот запущен')
print('Для запуска админ панели напишите "R".')
adm = input()
if adm == 'R':
    admin.panel('')


@bot.message_handler(commands=['start', 'restart'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton("Квас")
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть лохом и вашим рабом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    adm = input()
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 9999999)))
            if uv == 1:
                mem = message.from_user.first_name
                id = message.chat.id
                print(gen, mem, id)
                print('Запустить админ панель?(Y)')
                adm = input()
                if adm == 'Y':
                    admin.panel('')
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == 'Квас':
            bot.send_message(message.chat.id, 'Зря')
            if uv == 1:
                mem = message.from_user.first_name
                id = message.chat.id
                print(kv, mem, id)
                print('Запустить админ панель?(Y)')
                adm = input()
                if adm == 'Y':
                    admin.panel('')
            but = pymorphy2.MorphAnalyzer().parse('бутылка')[0]
            i = 99
            while i:
                bot.send_message(message.chat.id,
                                 f'В холодильнике {i} {but.make_agree_with_number(i).word} кваса. Возьмём одну и выпьем.')
                i -= 1
                if i % 10 == 1 and i != 11:
                    o = 'Осталась'
                else:
                    o = 'Осталось'
                bot.send_message(message.chat.id, f'{o} {i} {but.make_agree_with_number(i).word} кваса.')
            bot.send_message(message.chat.id, 'Было много кваса)')
        else:
            bot.send_message(message.chat.id, 'Харе спамить, я это не знаю.')
            if uv == 1:
                name = message.from_user.first_name
                id = message.chat.id
                print('Текст от ' + name + ' ' + str(id) + ': ' + message.text)
                print('Запустить админ панель?(Y)')
                adm = input()
                if adm == 'Y':
                    admin.panel('')
    if adm == 'R' or adm == 'Y':
        admin.panel('')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ОК")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
