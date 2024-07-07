import telebot
from telebot import types
import threading
from config import  main_menu_buttons, markup_main_menu, channels_id, channels_link, games, humster_buttons, hot_buttons, bcoin2048_buttons, blum_buttons, bitton_buttons, mtk_buttons, cats_buttons, fuel_buttons, zavod_buttons, memefi_buttons,vertus_buttons, tapswap_buttons, pixeltap_buttons, pocketfi_buttons,  cyber_finance_buttons, wave_wallet_mining_ocean_buttons, markup_games, memefi_markup,  mtk_markup, hot_markup, blum_markup, cats_markup,  fuel_markup, zavod_markup, bitton_markup, vertus_markup,  humster_markup, tapswap_markup, pocketfi_markup, bcoin2048_markup,  wave_wallet_mining_ocean_markup, cyber_finance_markup, pixeltap_markup
import re

print('!Bot is started')

TOKEN = '7327385734:AAFk35iDOjUMHzj47yv5ILmWxork0GL2Thk'

# для теста
# TOKEN = '7264048007:AAGvjW5AG_3oRn-CVHv2C8Q3yilkUs0bPxY'
# t.me/tetris_pekis_bot

user_states = {}

chat = ''
description = ''
timer = ''
cancel_message = 'Для доступа к боту необходимо подписаться на каналы, а после использовать команду /start ! \n' + channels_link[0] + '\n' + channels_link[1]

bot = telebot.TeleBot(TOKEN)

# start
@bot.message_handler(commands=['start'])
def start(message):
    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        bot.send_message(message.chat.id, 'Привет {0.first_name}, меня зовут ленивец - Чил. Я буду твоим персональным ассистентом. буду помогать тебе не забывать клеймить награды во всяких тапалках по типу ноткоина !' .format(message.from_user), reply_markup=markup_main_menu())
    else:
        bot.send_message(message.chat.id, 'Для доступа к боту необходимо подписаться на каналы! \n 1.Канал ' + channels_link[0] + '\n 2.Чат ' + channels_link[1] .format(message.from_user))
    
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

# сообщение с задержкой
def handle_delay(message,delay,text):
    chat_id = message.chat.id
    # Сообщение пользователю о запланированном отложенном сообщении
    bot.send_message(chat_id, f"Таймер запущен")
    # Вызов функции для отправки отложенного сообщения
    send_delayed_message(chat_id, text, delay)


# конвертация часов и минут в секунды
def convert_time_to_seconds(hours, minutes):
    return convert_hours_to_seconds(hours) + convert_minutes_to_seconds(minutes)

def convert_hours_to_seconds(hours):
    return hours * 3600

def convert_minutes_to_seconds(minutes):
    return minutes * 60

# /////////////////////////////////////////////////меню//////////////////////////////////////////////////////////
# меню
@bot.message_handler(func=lambda message: message.text in main_menu_buttons)
def handle_first_buttons(message):
    description = 'Этот бот создан с целью помощи людям, он будет напоминать вам заходить в игры и забирать награды. Если вы не обнаружили интересующий вас проект, вы можете написать нам об этом и мы его обязательно добавим. \n @dante_911  \n @Lioopa'
    feedback = 'По вопросам обратной связи и партнертсва пишите   \n @dante_911  \n @Lioopa'

    arr_buttons = main_menu_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
           
            bot.send_message(message.chat.id, description)
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, feedback)
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))






# /////////////////////////////////////////////////игры//////////////////////////////////////////////////////////
# таймер
@bot.message_handler(func=lambda message: message.text in games)
def handle_first_buttons(message):
    arr_buttons = games

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_main_menu())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, "🦥", reply_markup=blum_markup())
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, "🦥", reply_markup=humster_markup())
        elif message.text == arr_buttons[3]:
            bot.send_message(message.chat.id, "🦥", reply_markup=zavod_markup())
        elif message.text == arr_buttons[4]:
            bot.send_message(message.chat.id, "🦥", reply_markup=pocketfi_markup())
        elif message.text == arr_buttons[5]:
            bot.send_message(message.chat.id, "🦥", reply_markup=pixeltap_markup())
        elif message.text == arr_buttons[6]:
            bot.send_message(message.chat.id, "🦥", reply_markup=cats_markup())
        elif message.text == arr_buttons[7]:
            bot.send_message(message.chat.id, "🦥", reply_markup=bitton_markup())
        elif message.text == arr_buttons[8]:
            bot.send_message(message.chat.id, "🦥", reply_markup=hot_markup())
        elif message.text == arr_buttons[9]:
            bot.send_message(message.chat.id, "🦥", reply_markup=mtk_markup())
        elif message.text == arr_buttons[10]:
            bot.send_message(message.chat.id, "🦥", reply_markup=bcoin2048_markup())
        elif message.text == arr_buttons[11]:
            bot.send_message(message.chat.id, "🦥", reply_markup=cyber_finance_markup())
        elif message.text == arr_buttons[12]:
            bot.send_message(message.chat.id, "🦥", reply_markup=memefi_markup())
        elif message.text == arr_buttons[13]:
            bot.send_message(message.chat.id, "🦥", reply_markup=vertus_markup())
        elif message.text == arr_buttons[14]:
            bot.send_message(message.chat.id, "🦥", reply_markup=fuel_markup())
        elif message.text == arr_buttons[15]:
            bot.send_message(message.chat.id, "🦥", reply_markup=tapswap_markup())
        elif message.text == arr_buttons[16]:
            bot.send_message(message.chat.id, "🦥", reply_markup=wave_wallet_mining_ocean_markup())
        
        
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))




# humster
@bot.message_handler(func=lambda message: message.text in humster_buttons)
def handle_first_buttons(message):
    chat = '[Hamster Kombot](https://t.me/hamster_kombat_chat)'
    description = '[Hamster Kombot](https://t.me/hamster_kombaT_bot/start?startapp=kentId1901528332) — это игра в жанре кликер, в которую можно играть в мессенджере Telegram. В ней предлагается превратить хомяка в гендиректора успешной компании, кликая на монетку (отсюда и название — кликер) и покупая карточки улучшения.'
    timer = 'Пора почесать свою мохнатку \n https://t.me/hamster_kombaT_bot/start?startapp=kentId1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = humster_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 3
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# blum
@bot.message_handler(func=lambda message: message.text in blum_buttons)
def handle_first_buttons(message):
    chat = '[Blum](https://t.me/blumcrypto)'
    description = '[Blum](t.me/BlumCryptoBot/app?startapp=ref_TvS5V1tzQv) Crypto — это гибридная биржа, обеспечивающая легкий доступ к любым монетам и токенам, а также простым деривативам через мини-приложение Telegram. Это мини-игра в Telegram, в котором пользователям доступен фарм Points, это же в будущем токен.'
    timer = 'Я хоть и не феечка, но пора меня потыкать... \n t.me/BlumCryptoBot/app?startapp=ref_TvS5V1tzQv \n Не забудь повторно установить таймер'
    
    arr_buttons = blum_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 8
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# hot
@bot.message_handler(func=lambda message: message.text in hot_buttons)
def handle_first_buttons(message):
    chat = '[Hot](https://t.me/hotonnear)'
    description = '[HOT](https://t.me/herewalletbot/app?startapp=9415231) - это центральный элемент экосистемы NEAR внутри Telegram. Благодаря мета-транзакциям использование HOT позволяет совершать реальные транзакции на блокчейне, играть в игры и оплачивать переводы. Это первая FT, которая обладает функциональностью нативных токенов блокчейна L1'
    timer = 'Пора подкинуть дров 🔥 \n https://t.me/herewalletbot/app?startapp=9415231 \n Не забудь повторно установить таймер'
    
    

    arr_buttons = hot_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 0
            minutes = 3
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user)) 




# PocketFi
@bot.message_handler(func=lambda message: message.text in pocketfi_buttons)
def handle_first_buttons(message):
    chat = '[PocketFi](https://t.me/pocketfi)'
    description = '[PocketFi](t.me/pocketfi_bot/Mining?startapp=1901528332) — отличное решение для кроссчейн переводов, обменов, а также снайпинга и копитрейдинга. Оно призвано упростить взаимодействие с DeFi при помощи Telegram и платформы Mini Apps. С ним можно обменивать токены и зарабатывать на снайпинге. Простыми словами вы можете обменять токены TON на ETH и т.д.'
    timer = 'Крути лудильню \n t.me/pocketfi_bot/Mining?startapp=1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = pocketfi_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 5
            minutes = 55
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# PixelTap
@bot.message_handler(func=lambda message: message.text in pixeltap_buttons)
def handle_first_buttons(message):
    chat = '[PixelTap](https://t.me/pixelverse_xyz)'
    description = '[PixelTap](https://t.me/pixelversexyzbot?start=1901528332) - это приложение не только для майнинга будущего токена PIXFI, с последующим аирдропом, но и игра, в которой ты становишься частью игровых событий. Разве это неудивительно?'
    timer = 'Пора уничтожить пикслели \n https://t.me/pixelversexyzbot?start=1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = pixeltap_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 8
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# zavod
@bot.message_handler(func=lambda message: message.text in zavod_buttons)
def handle_first_buttons(message):
    chat = '[Zavod](https://t.me/mdaowallet_telegram_chat)'
    description = 'MDAO Telegram Wallet предлагает весьма необычный способ заработка - работу на [Zavod](https://t.me/Marswallet_bot?start=ref_1901528332). Этот завод открылся и разыскивает работников на самые базовые должности. Обещают сдельную оплату, но забудьте о кофе и печеньях - их здесь нет.'
    timer = 'Крипта для лохов, завод тема норм пацанов \n https://t.me/mdaowallet_telegram_chat \n Не забудь повторно установить таймер'
    
    arr_buttons = zavod_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 0
            minutes = 1
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# cats
@bot.message_handler(func=lambda message: message.text in cats_buttons)
def handle_first_buttons(message):
    chat = '[Catizen](https://t.me/CatizenAI/1)'
    description = '[Catizen](https://t.me/catizenbot/gameapp?startapp=r_1312_2420164) AI — это проект Play to Airdrop, сочетающий в себе Metaverse, Game Fi и Ai. Команда Catizen Ai заключила партнерское соглашение с Ton Fish, чтобы сделать экосистему Metaverse доступной для большего числа пользователей.'
    timer = 'Пора поческать своих кисок \n https://t.me/catizenbot/gameapp?startapp=r_1312_2420164 \n Не забудь повторно установить таймер'
    
    arr_buttons = cats_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 8
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# биттон
@bot.message_handler(func=lambda message: message.text in bitton_buttons)
def handle_first_buttons(message):
    chat = '[Bitton](https://t.me/bittonapp)'
    description = 'Криптовалюта [Bitton](https://t.me/bittonapp_bot?start=eq86dih4) – это часть новой игровой экосистемы в «Телеграмм», в которой каждый клик по телефону позволяет бесплатно добыть сразу два токена: BTC и BTN. В этом обзоре мы разберем, чего ждать пользователям от тапалки Bitton и как люди зарабатывают через данный бот в “Телеграмм”.'
    timer = 'Потыкай монету, а то она уже залежалась \n (https://t.me/bittonapp_bot?start=eq86dih4 \n Не забудь повторно установить таймер'
    
    arr_buttons = bitton_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 24
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))



# mtk
@bot.message_handler(func=lambda message: message.text in mtk_buttons)
def handle_first_buttons(message):
    chat = '[MTK](https://t.me/metatokens_mtk)'
    description = '[MTK](https://t.me/mtkbossbot?start=ref1901528332) CLICKER MAFIA - кликер от казино METATOKENS, где каждый игрок становится его совладельцем.'
    timer = 'Кажется ты задолжал нам крумную сумму деняг...\n https://t.me/mtkbossbot?start=ref1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = mtk_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 2
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# bcoin2048
@bot.message_handler(func=lambda message: message.text in bcoin2048_buttons)
def handle_first_buttons(message):
    chat = '[Bcoin2048](https://t.me/bcoin2048)'
    description = '[Bcoin](https://t.me/Bcoin2048bot/app?startapp=ref_pCGp_C-12nFdKZCldsgWLLes) - всеми известная игра в 2048 вышла в мире web3'
    timer = 'Прошло 21600 секунд,а ты до сих пор не собрал 2048 \n https://t.me/Bcoin2048bot/app?startapp=ref_pCGp_C-12nFdKZCldsgWLLes \n Не забудь повторно установить таймер'
    
    arr_buttons = bcoin2048_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 6
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))



# cyber finance
@bot.message_handler(func=lambda message: message.text in cyber_finance_buttons)
def handle_first_buttons(message):
    chat = '[cyber finance](https://t.me/CyberFinanceChat)'
    description = '[Cyber Finance](https://t.me/CyberFinanceBot?start=cj1xaXE0ejk3Y2dZMjcmdT1yZWY=) - это DeFi для высокой доходности и  ликвидности, доступный непосредственно в Telegram. '
    timer = 'Настало время разить яйцо \n https://t.me/CyberFinanceBot?start=cj1xaXE0ejk3Y2dZMjcmdT1yZWY= \n Не забудь повторно установить таймер'
    
    arr_buttons = cyber_finance_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 0
            minutes = 1
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# memefi
@bot.message_handler(func=lambda message: message.text in memefi_buttons)
def handle_first_buttons(message):
    chat = '[memefi](https://t.me/memeficlub)'
    description = '[MemeFi](https://t.me/memefi_coin_bot?start=r_b55dbd1a8f) функционирует по принципу, схожему с NotCoin: нужно кликать по экрану, прокачивать аккаунт, копить монеты и выполнять особые задания. Уникальность MemeFi заключается в собственной сказочной истории, которая делает игру значительно интереснее.'
    timer = 'Пора вернуться на сказочное болото и надавать всем по щам \n https://t.me/memefi_coin_bot?start=r_b55dbd1a8f \n Не забудь повторно установить таймер'
    
    arr_buttons = memefi_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 3
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# vertus
@bot.message_handler(func=lambda message: message.text in vertus_buttons)
def handle_first_buttons(message):
    chat = '[Vertus](https://t.me/thevertus_chat)'
    description = '[Vertus](https://t.me/vertus_app_bot/app?startapp=1901528332)- это децентрализованное Web3-приложение, которое построено на блокчейне TON и доступно напрямую через Телеграмм. В самой игре мы добываем токены $VERT, которых в будущем ожидает листинг (по заверению разработчиков).'
    timer = 'Не забывай про деревню \n https://t.me/vertus_app_bot/app?startapp=1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = vertus_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 2
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# fuel
@bot.message_handler(func=lambda message: message.text in fuel_buttons)
def handle_first_buttons(message):
    chat = '[Fuel](https://t.me/fueljetton)'
    description = '[Fuel](https://t.me/fueljetton_bot/app?startapp=1901528332) Jetton - это полностью бесплатная игра на популярном блокчейне TON, в которой нужно майнить нефть (Fuel Mining) или по-нашему добывать нефть (топливо).'
    timer = 'Пора пампить нефть \n https://t.me/fueljetton_bot/app?startapp=1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = fuel_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 12
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# tapswap
@bot.message_handler(func=lambda message: message.text in tapswap_buttons)
def handle_first_buttons(message):
    chat = '[Tapswap](https://t.me/tapswap)'
    description = '[TapSwap](https://t.me/tapswap_mirror_1_bot?start=r_1901528332) — это игра-кликер в Telegram, позволяющая пользователям зарабатывать виртуальные токены с помощью различных функций майнинга в приложении. Это очередная тапалка на блокчейне TON, которых уже было несколько к сегодняшнему дню. '
    timer = 'Пора потапать \n https://t.me/tapswap_mirror_1_bot?start=r_1901528332 \n Не забудь повторно установить таймер'
    
    arr_buttons = tapswap_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 0
            minutes = 1
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = 'Напиши свое время в минутах(только цифру): \n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин\n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин \n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# Wave Wallet mining Ocean
@bot.message_handler(func=lambda message: message.text in wave_wallet_mining_ocean_buttons)
def handle_first_buttons(message):
    chat = '[Wave Wallet mining Ocean](https://t.me/wave_announcements)'
    description = '[Wave Walley](t.me/waveonsuibot/walletapp?startapp=5066328)— это многофункциональный (в обозримом будущем) кошелёк с возможностью майнинга токена $OCEAN. Сам кошелёк разработан на блокчейне SUI, что уже не может не радовать, транзакции в сети SUI практически моментальные + мизерные комиссии, имеет довольно простой и интуитивно понятный интерфейс.'
    timer = 'Запрыгивай на волну \n https://t.me/waveonsuibot?startapp=5066328 \n Не забудь повторно установить таймер'
    
    arr_buttons = wave_wallet_mining_ocean_buttons

    if check_sub(message=message, id=channels_id[0]) == True and check_sub(message=message, id=channels_id[1]) == True:
        if message.text == arr_buttons[0]:
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[1]:
            bot.send_message(message.chat.id, chat .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[2]:
            bot.send_message(message.chat.id, description .format(message.from_user), parse_mode='Markdown')
        elif message.text == arr_buttons[3]:
            hours = 2
            minutes = 0
            handle_delay(message, convert_time_to_seconds(hours=hours, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())
        elif message.text == arr_buttons[4]:
            user_states[message.chat.id] = timer
            self_timer = '.х:\n 1 час = 60 мин \n2 часа = 120 мин\n3 часа = 180 мин \n4 часа = 240 мин \n5 часов = 300 мин \n6 часов = 360 мин \n7 часов = 420 мин \n8 часов = 480 мин \n9 часов = 540 мин\n10 часов = 600 мин \n11 часов = 660 мин \n12 часов = 720 мин'
            bot.send_message(message.chat.id, self_timer .format(message.from_user))
    else:
        bot.send_message(message.chat.id, cancel_message .format(message.from_user))


# свой таймер
@bot.message_handler(func=lambda message: True)
def self_timer_func(message):
    check = lambda s: not all('0'<=x<='9' for x in s.lower())
    if check(message.text) == False:
        minutes = int(message.text)
        timer = user_states[message.chat.id]
        if timer != '':
            handle_delay(message, convert_time_to_seconds(hours=0, minutes=minutes), timer)
            bot.send_message(message.chat.id, "🦥", reply_markup=markup_games())


bot.polling(none_stop = True, interval =0) 