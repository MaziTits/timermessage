import telebot
from telebot import types
import threading
from config import channels_name, channels_id, channels_link

TOKEN = '7366677041:AAED17dQSi-4dIz2_fGCiA-YzL3r8H3qRbg'

bot = telebot.TeleBot(TOKEN)

# start
@bot.message_handler(commands=['start'])
def start(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        bot.send_message(message.chat.id, 'Привет, это бот напоминалка. Он помогает тебе не забывать клеймить награды во всяких хуйнях по типу ноткоина {0.first_name}!' .format(message.from_user), reply_markup=markup())
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

# проверка подписки
def check_sub(message, id):
  user_id = message.from_user.id
  memeber = bot.get_chat_member(id, user_id)
  if memeber.status in ['member', 'administrator', 'creator']:
    return True
  else:
    return False

# отправка сообщения с задержкой (таймер)
def send_delayed_message(chat_id, text, delay):
    def task():
        bot.send_message(chat_id, text)
    # Создание и запуск таймера
    threading.Timer(delay, task).start()

def handle_delay(message,delay,text):
    chat_id = message.chat.id
    # Сообщение пользователю о запланированном отложенном сообщении
    bot.send_message(chat_id, f"Сообщение будет отправлено через {delay} секунд.")
    # Вызов функции для отправки отложенного сообщения
    send_delayed_message(chat_id, text, delay)

# маркап игр
def markup():
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = types.KeyboardButton('Хомяк')
  itemBL = types.KeyboardButton('Blum')
  itemhot = types.KeyboardButton('Hot')
  markup.add(item1,itemBL,itemhot)
  return markup

# маркап хомяк
def two_markup():
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    info = types.KeyboardButton('Информация о проекте')
    item3h = types.KeyboardButton('3 часа')
    chat = types.KeyboardButton('чат')
    back = types.KeyboardButton('Назад')
    markyp_reply.add(info,chat,item3h,back,)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in ['','Хомяк', 'Назад', '3 часа', 'чат', 'Информация о проекте'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=two_markup())
        elif message.text == 'Хомяк':
            bot.send_message(message.chat.id, "🐨", reply_markup=two_markup())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "🐨", reply_markup=markup())
        elif message.text =='Информация о проекте':
            bot.send_message(message.chat.id, " Hamster Kombat — это игра в жанре кликер, в которую можно играть в мессенджере Telegram. В ней предлагается превратить хомяка в гендиректора успешной компании, кликая на монетку (отсюда и название — кликер) и покупая карточки улучшения.https://t.me/hamster_kombaT_bot/start?startapp=kentId1901528332" .format(message.from_user))
        elif message.text =='3 часа':
            handle_delay(message,3, 'Пора почесать свою мохнатку')
        elif message.text =='чат':
            bot.send_message(message.chat.id, "https://t.me/hamster_kombat_chat" .format(message.from_user))
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

# маркап блюм
def blum_markup():
    
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item5h = types.KeyboardButton('8 часов')
    back = types.KeyboardButton('Назад')
    info = types.KeyboardButton('Информация о BLUM')
    chat = types.KeyboardButton('чат Blum')
    markyp_reply.add(info,chat,item5h,back)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in  ['','Blum', 'Назад', '8 часов', 'чат Blum','Информация о BLUM'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=blum_markup())   
        elif message.text == 'Blum':
            bot.send_message(message.chat.id,"🐨",  reply_markup=blum_markup())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "🐨", reply_markup=markup())
        elif message.text =='чат Blum':
            bot.send_message(message.chat.id, "https://t.me/blumcrypto" .format(message.from_user))
        elif message.text =='Информация о BLUM':
            bot.send_message(message.chat.id, "Blum Crypto — это гибридная биржа, обеспечивающая легкий доступ к любым монетам и токенам, а также простым деривативам через мини-приложение Telegram. Это мини-игра в Telegram, в котором пользователям доступен фарм Points, это же в будущем токен.t.me/BlumCryptoBot/app?startapp=ref_TvS5V1tzQv" .format(message.from_user))
        elif message.text =='8 часов':
            handle_delay(message,3, 'Я хоть и не феечка, но пора меня потыкать... @BlumCryptoBot')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

# маркап hot
def hot_markup():
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    itemhot = types.KeyboardButton('2 часа')
    back = types.KeyboardButton('Назад')
    info = types.KeyboardButton('Информация о Hot')
    chat = types.KeyboardButton('Чат Hot')
    
    markyp_reply.add(info,chat,itemhot,back)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in  ['','Hot', 'Назад', '2 часа','Чат Hot','Информация о Hot'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
                bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=hot_markup())
        elif message.text == 'Hot':
                bot.send_message(message.chat.id,"🐨", reply_markup=hot_markup())
        elif message.text == 'Назад':
                bot.send_message(message.chat.id, "🐨",reply_markup=markup())
        elif message.text =='чат HOT':
            bot.send_message(message.chat.id, "https://t.me/hotonnear" .format(message.from_user))
        elif message.text =='Информация о BLUM':
            bot.send_message(message.chat.id, "HOT - это центральный элемент экосистемы NEAR внутри Telegram. Благодаря мета-транзакциям использование HOT позволяет совершать реальные транзакции на блокчейне, играть в игры и оплачивать переводы. Это первая FT, которая обладает функциональностью нативных токенов блокчейна L1.https://t.me/herewalletbot/app?startapp=9415231" .format(message.from_user))
            bot.send_message(message.chat.id,  reply_markup=hot_markup())
        elif message.text =='2 часа':
            handle_delay(message,3, 'Пора и дров подкинуть @herewalletbot')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

bot.polling(none_stop = True, interval =0) 