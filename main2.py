import telebot
from telebot import types
import threading
from config import channels_name, channels_id, channels_link



TOKEN = '7327385734:AAFk35iDOjUMHzj47yv5ILmWxork0GL2Thk'

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

# вызов отправки сообщения с задержкой (таймер)
def send_delayed_message(chat_id, text, delay):
    def task():
        bot.send_message(chat_id, text)
    # Создание и запуск таймера
    threading.Timer(delay, task).start()

# сообщение с задержко
def handle_delay(message,delay,text):
    chat_id = message.chat.id
    # Сообщение пользователю о запланированном отложенном сообщении
    bot.send_message(chat_id, f"Таймер запущен")
    # Вызов функции для отправки отложенного сообщения
    send_delayed_message(chat_id, text, delay)

# маркап игр
def markup():
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = types.KeyboardButton('Хомяк')
  itemBL = types.KeyboardButton('Blum')
  itemhot = types.KeyboardButton('Hot')
  itemzavod = types.KeyboardButton('Zavod')
  itempoket = types.KeyboardButton('PocketFi')
  itempixel = types.KeyboardButton('PixelTap')
  markup.add(item1,itemBL,itemhot,itemzavod,itempoket,itempixel)
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
            bot.send_message(message.chat.id, " [Hamster Kombot](https://t.me/hamster_kombaT_bot/start?startapp=kentId1901528332) — это игра в жанре кликер, в которую можно играть в мессенджере Telegram. В ней предлагается превратить хомяка в гендиректора успешной компании, кликая на монетку (отсюда и название — кликер) и покупая карточки улучшения." .format(message.from_user), parse_mode='Markdown')
        elif message.text =='3 часа':
            handle_delay(message,10800, 'Пора почесать свою мохнатку  [Hamster Kombot](https://t.me/hamster_kombaT_bot/start?startapp=kentId1901528332)')
        elif message.text =='чат':
            bot.send_message(message.chat.id,"[Hamster Kombot](https://t.me/hamster_kombat_chat)" .format(message.from_user), parse_mode='Markdown')
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
            bot.send_message(message.chat.id, "[Blum](https://t.me/blumcrypto)" .format(message.from_user),parse_mode='Markdown')
        elif message.text =='Информация о BLUM':
            bot.send_message(message.chat.id, "[Blum](t.me/BlumCryptoBot/app?startapp=ref_TvS5V1tzQv) Crypto — это гибридная биржа, обеспечивающая легкий доступ к любым монетам и токенам, а также простым деривативам через мини-приложение Telegram. Это мини-игра в Telegram, в котором пользователям доступен фарм Points, это же в будущем токен." .format(message.from_user),parse_mode='Markdown')
        elif message.text =='8 часов':
            handle_delay(message,28800, 'Я хоть и не феечка, но пора меня потыкать...[Blum](t.me/BlumCryptoBot/app?startapp=ref_TvS5V1tzQv)')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

# маркап hot
def hot_markup():
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    itemhot = types.KeyboardButton('2 часа')
    back = types.KeyboardButton('Назад')
    info = types.KeyboardButton('Информация о Hot')
    chat = types.KeyboardButton('Чат HOT')
    
    markyp_reply.add(info,chat,itemhot,back)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in  ['','Hot', 'Назад', '2 часа', 'Чат HOT','Информация о Hot'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=hot_markup())   
        elif message.text == 'Hot':
            bot.send_message(message.chat.id,"🐨",  reply_markup=hot_markup())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "🐨", reply_markup=markup())
        elif message.text =='Чат HOT':
            bot.send_message(message.chat.id, "[Hot](https://t.me/hotonnear)" .format(message.from_user),parse_mode='Markdown')
        elif message.text =='Информация о Hot':
            bot.send_message(message.chat.id, "[HOT](https://t.me/herewalletbot/app?startapp=9415231) - это центральный элемент экосистемы NEAR внутри Telegram. Благодаря мета-транзакциям использование HOT позволяет совершать реальные транзакции на блокчейне, играть в игры и оплачивать переводы. Это первая FT, которая обладает функциональностью нативных токенов блокчейна L1  " .format(message.from_user),parse_mode='Markdown')
        elif message.text =='2 часа':
            handle_delay(message,7200, 'Пора подкинуть дров 🔥 [HOT](https://t.me/herewalletbot/app?startapp=9415231)')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

# маркап PocketFi
def PocketFi_markup():
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    itemhot = types.KeyboardButton('5:45 часов')
    back = types.KeyboardButton('Назад')
    info = types.KeyboardButton('Информация о Pocketfi')
    chat = types.KeyboardButton('Чат PocketFi')
    
    markyp_reply.add(info,chat,itemhot,back)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in  ['','PocketFi', 'Назад', '5:45 часов', 'Чат PocketFi','Информация о Pocketfi'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=PocketFi_markup())   
        elif message.text == 'PocketFi':
            bot.send_message(message.chat.id,"🐨",  reply_markup=PocketFi_markup())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "🐨", reply_markup=markup())
        elif message.text =='Чат PocketFi':
            bot.send_message(message.chat.id, "[PocketFi](https://t.me/pocketfi)" .format(message.from_user),parse_mode='Markdown')
        elif message.text =='Информация о Pocketfi':
            bot.send_message(message.chat.id, "[PocketFi](t.me/pocketfi_bot/Mining?startapp=1901528332) — отличное решение для кроссчейн переводов, обменов, а также снайпинга и копитрейдинга. Оно призвано упростить взаимодействие с DeFi при помощи Telegram и платформы Mini Apps. С ним можно обменивать токены и зарабатывать на снайпинге. Простыми словами вы можете обменять токены TON на ETH и т.д. " .format(message.from_user),parse_mode='Markdown')
        elif message.text =='5:45 часов':
            handle_delay(message,20700, 'Крути колесо  [PocketFi](t.me/pocketfi_bot/Mining?startapp=1901528332)')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))


# маркап PixelTap
def PixelTap_markup():
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    itemhot = types.KeyboardButton('8 часов👾')
    back = types.KeyboardButton('Назад')
    info = types.KeyboardButton('Информация о PixelTap')
    chat = types.KeyboardButton('Чат PixelTap')
    
    markyp_reply.add(info,chat,itemhot,back)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in  ['','PixelTap', 'Назад', '8 часов👾', 'Чат PixelTap','Информация о PixelTap'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=PixelTap_markup())   
        elif message.text == 'PixelTap':
            bot.send_message(message.chat.id,"🐨",  reply_markup=PixelTap_markup())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "🐨", reply_markup=markup())
        elif message.text =='Чат PixelTap':
            bot.send_message(message.chat.id, "[PixelTap](https://t.me/pixelverse_xyz)" .format(message.from_user),parse_mode='Markdown')
        elif message.text =='Информация о PixelTap':
            bot.send_message(message.chat.id, "[PixelTap](https://t.me/pixelversexyzbot?start=1901528332) - это приложение не только для майнинга будущего токена PIXFI, с последующим аирдропом, но и игра, в которой ты становишься частью игровых событий. Разве это неудивительно?  " .format(message.from_user),parse_mode='Markdown')
        elif message.text =='8 часов👾':
            handle_delay(message,28800, 'Пора потыкать на пикслели @pixelversexyzbot')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))

# маркап Zavod
def Zavod_markup():
    markyp_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
    itemhot = types.KeyboardButton('2 часа🏗️')
    back = types.KeyboardButton('Назад')
    info = types.KeyboardButton('Информация о Zavod')
    chat = types.KeyboardButton('Чат Zavod')
    
    markyp_reply.add(info,chat,itemhot,back)
    return markyp_reply

# обработчики событий кнопок
@bot.message_handler(func=lambda message: message.text in  ['','Zavod', 'Назад', '2 часа🏗️', 'Чат Zavod','Информация о Zavod'])
def handle_first_buttons(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, "Вы нажали Кнопка 1. Теперь выберите следующую кнопку:", reply_markup=Zavod_markup())   
        elif message.text == 'Zavod':
            bot.send_message(message.chat.id,"🐨",  reply_markup=Zavod_markup())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "🐨", reply_markup=markup())
        elif message.text =='Чат Zavod':
            bot.send_message(message.chat.id, "[Zavod](https://t.me/mdaowallet_telegram_chat)" .format(message.from_user),parse_mode='Markdown')
        elif message.text =='Информация о Zavod':
            bot.send_message(message.chat.id, "MDAO Telegram Wallet предлагает весьма необычный способ заработка - работу на [Zavod](https://t.me/Marswallet_bot?start=ref_1901528332). Этот завод открылся и разыскивает работников на самые базовые должности. Обещают сдельную оплату, но забудьте о кофе и печеньях - их здесь нет.  " .format(message.from_user),parse_mode='Markdown')
        elif message.text =='2 часа🏗️':
            handle_delay(message,7200, 'Крипта для лохов, завод тема норм пацанов [Zavod](https://t.me/Marswallet_bot?start=ref_1901528332)')
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n' + channels_link[0] + '\n' + channels_link[1] .format(message.from_user))



bot.polling(none_stop = True, interval =0) 