import telebot
import pymorphy2
import config
import random
from telebot import types
from threading import Thread
from time import sleep
gen = 'Сгенерировал(а)'
kv = 'Квас начал(а)'
print('Бот запущен')
print('Вас приветствует админ-панель.')
OTV = False
mes = 0
otv = ''
calll = 0
Adm = 0
udal = 2
uv = 1
admin = 0
soob = []
admins = [663414562]
bot = telebot.TeleBot(config.TOKEN)
def mainbot():
    global OTV
    global otv
    global bot
    @bot.message_handler(commands=['start', 'restart'])
    def welcome(message):
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("Квас")
        item1 = types.KeyboardButton("Случайное число")
        item2 = types.KeyboardButton("Как дела?")
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный, чтобы быть.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['admin'])
    def inbotpanel(message):
        global soob
        global admin
        global admins
        if message.chat.id in admins:
          mem = message.from_user.first_name
          markup1 = types.InlineKeyboardMarkup(row_width=2)
          item4 = types.InlineKeyboardButton("Выход", callback_data='exit')
          item3 = types.InlineKeyboardButton("Ответить человеку", callback_data='OTV')
          item1 = types.InlineKeyboardButton("Все сообщения", callback_data='soobx')
          item2 = types.InlineKeyboardButton("Удалить сообшения", callback_data='minsoobx')
          item5 = types.InlineKeyboardButton("Выключить уведомления", callback_data='S_OFF')
          item6 = types.InlineKeyboardButton("Включить уведомления", callback_data='S_ON')
          item7 = types.InlineKeyboardButton("Удалить админа", callback_data='MDA')
          item8 = types.InlineKeyboardButton("Добавить админа", callback_data='DA')
          markup1.add(item1, item2, item3, item5, item6, item7, item8, item4)
          bot.send_message(message.chat.id, f'Добро пожаловать в админ-панель, {mem}!', reply_markup=markup1)
          id = message.chat.id
          if uv == 1:
            soob.append(f'{mem}, {id} зашёл в админ-панель.')
            print(f'{mem}, {id} зашёл в админ-панель.')
          admin = 1
        else:
          mem = message.from_user.first_name
          bot.send_message(message.chat.id, f'Вы не админ, {mem}!')

    def adminkatext(message):
      global otv
      global calll
      global admin
      if calll == 1 and message.chat.id in admins:
        id1 = message.text
        telebot.TeleBot.send_message(bot, int(id1), "Админ написал вам:")
        telebot.TeleBot.send_message(bot, int(id1), otv)
        calll = 0
        admin = 0
    @bot.message_handler(content_types=['text'])
    def lalala(message):
        global otv
        global soob
        global Adm
        global admins
        global udal
        if message.chat.type == 'private':
          if calll == 1 and message.chat.id in admins:
            otv = message.text
            msg = bot.reply_to(message, "Введите ID")
            bot.register_next_step_handler(msg, adminkatext)
          if Adm == 1 and message.chat.id in admins:
            id1 = message.text
            if udal == 1:
              admins.remove(int(id1))
               bot.send_message(message.chat.id, f'{id1} удалён(а) из админов.')
              udal = 2
            elif udal == 0:
              admins.append(int(id1))
              bot.send_message(message.chat.id, f'{id1} добавлен(а) к админам.')
              udal = 2
          else:
            if message.text == 'Случайное число':
                bot.send_message(message.chat.id, str(random.randint(0, 9999999)))
                if uv == 1:
                    mem = message.from_user.first_name
                    id = message.chat.id
                    soob.append(f'{gen} {mem} {id}')
                    print(gen, mem, id)
            elif message.text == 'Как дела?':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
                item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

                markup.add(item1, item2)

                bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
            elif message.text == 'Квас':
                bot.send_message(message.chat.id, 'Так как квас крашит бота из-за коровавируса (COROV-19), квас был замедлен.')
                
                if uv == 1:
                    mem = message.from_user.first_name
                    id = message.chat.id
                    soob.append(f'{kv} {mem} {id}')
                    print(kv, mem, id)
                but = pymorphy2.MorphAnalyzer().parse('бутылка')[0]
                i = 99
                while i:
                    bot.send_message(message.chat.id,
                                     f'В холодильнике {i} {but.make_agree_with_number(i).word} кваса. Возьмём одну и выпьем.')
                    i -= 1
                    sleep(0.5)
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
                    soob.append(f'Текст от {name} {str(id)}: {message.text}')
                    print('Текст от ' + name + ' ' + str(id) + ': ' + message.text)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        global admin
        global soob
        global calll
        global admins
        global Adm
        global uv
        global udal
        try:
            if call.message:
              if admin == 1 and call.message.chat.id in admins:
                if call.data == 'soobx':
                  if len(soob) == 0:
                    id = call.message.chat.id
                    telebot.TeleBot.send_message(bot, id, 'Сообщений нет')
                  else:
                    for i in range(len(soob)):
                      id = call.message.chat.id
                      telebot.TeleBot.send_message(bot, id, soob[i])
                    
                elif call.data == 'minsoobx':
                    soob = []
                    id = call.message.chat.id
                    telebot.TeleBot.send_message(bot, id, 'Сообщения удалены.')
                elif call.data == 'exit':
                    id = call.message.chat.id
                    mem = call.from_user.first_name
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"До свидания, {mem}!", reply_markup=None)
                    if uv == 1:
                      soob.append(f'{mem}, {id} вышел из админ-панели.')
                      print(f'{mem}, {id} вышел из админ-панели.')
                    admin = 0
                elif call.data == 'OTV':
                  bot.send_message(call.message.chat.id, 'Напишите сообщение:')
                  calll = 1
                elif call.data == 'DA':
                  bot.send_message(call.message.chat.id, 'Id человека:')
                  Adm = 1
                  udal = 0
                elif call.data == 'MDA':
                  bot.send_message(call.message.chat.id, 'Id человека:')
                  Adm = 1
                  udal = 1
                elif call.data == 'S_OFF':
                  bot.send_message(call.message.chat.id, 'Уведомления выключены')
                  uv = 0
                elif call.data == 'S_ON':
                  bot.send_message(call.message.chat.id, 'Уведомления включены')
                  uv = 1
              else:
                if call.data == 'good':
                    bot.send_message(call.message.chat.id, 'Вот и отличненько')
                elif call.data == 'bad':
                    bot.send_message(call.message.chat.id, 'Бывает')

                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Как дела?",
                                      reply_markup=None)

                # show alert
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="ОК")

        except Exception as e:
            print(repr(e))

    bot.polling(none_stop=True)

def panel():
    global uv
    global bot
    global OTV
    print('H: Помощь')
    kv = 0
    while kv != 1:
        adm = input()
        if adm == "S_OFF":
            uv = 0
            print('Умедомления отключены')
        elif adm == "S_ON":
            uv = 1
            print('Умедомления включены')
        elif adm == 'OTV':
          ch = input('id:')
          b = input('Сообщение:')
          telebot.TeleBot.send_message(bot, ch, "Админ написал вам:")
          telebot.TeleBot.send_message(bot, ch, b)
        elif adm == 'DA':
          admins.append(int(input('Id человека:')))
          print('Успешно добавлен(а)')
        elif adm == 'MDA':
          admins.remove(int(input('Id человека:')))
          print('Успешно удалён(а)')
        elif adm == 'H':
            print('S_OFF: отключить все уведомления')
            print('S_ON: включить все уведомления')
            print('OTV: ответить человеку')
            print('DA: Добавить админа до перезагрузки бота')
            print('MDA: Удалить админа')


if __name__ == '__main__':
    p1 = Thread(target=panel)
    p2 = Thread(target=mainbot)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
