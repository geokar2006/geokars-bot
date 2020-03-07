import telebot
import pymorphy2
import config
import random
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
gen = 'Сгенерировал'
tb = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start', 'restart'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item3 = types.KeyboardButton("Квас")
	item1 = types.KeyboardButton("Рандомное число")
	item2 = types.KeyboardButton("Как дела?")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть лохом и вашим рабом.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Рандомное число':
		   bot.send_message(message.chat.id, str(random.randint(0,9999999)))
		   mem = message.from_user.first_name
		   print(gen, mem)
		elif message.text == 'Как дела?':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		elif message.text == 'Квас':
			but = pymorphy2.MorphAnalyzer().parse('бутылка')[0]
			i = 99
			while i:
				bot.send_message(message.chat.id, f'В холодильнике {i} {but.make_agree_with_number(i).word} кваса. Возьмём одну и выпьем.')
				i -= 1
				if i % 10 == 1 and i != 11:
					o = 'Осталась'
				else:
					o = 'Осталось'
				bot.send_message(message.chat.id, f'{o} {i} {but.make_agree_with_number(i).word} кваса.')
			bot.send_message(message.chat.id, 'Было много кваса)')
		else:
			bot.send_message(message.chat.id, 'Харе спамить, я это не знаю.')
			name = message.from_user.first_name
			id = message.chat.id
			print('Текст от ' + name + ' ' + str(id) + ': ' + message.text)
			print('Ответить?(Y)')
			a = input()
			if a == 'Y':
			    b = input('Сообщение:')
			    id = input('id:')
			    bot.send_message(message.chat.id, 'Админ ответил вам: ' + b)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО")

    except Exception as e:
        print(repr(e))
# RUN
bot.polling(none_stop=True)