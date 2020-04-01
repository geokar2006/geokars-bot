import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


class admin:
    def panel(self):
        print('S_OFF: отключить все уведомления')
        print('S_ON: включить все уведомления')
        print('OTV: ответить человеку')
        kv = 0
        while kv != 1:
            adm = input()
            if adm == "S_OFF":
                uv = 0
                print('Умедомления отключены')
                break
            elif adm == "S_ON":
                uv = 1
                print('Умедомления включены')
                break
            elif adm == 'OTV':
                b = input('Сообщение:')
                id1 = input('id:')

                @bot.message_handler(content_types=[])
                def OTV(message):
                    id = id1
                    bot.send_message(message.chat.id, 'Админ написал вам:')
                    bot.send_message(message.chat.id, f'{b} ')

                break
