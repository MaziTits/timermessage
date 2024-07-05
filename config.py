import telebot
from telebot import types


# stable
# channels_name = ["SinopsisBTC Чат", "spiboba320"]
# channels_id = [-1001854259380, -1002213476974]
# channels_link = ["[Sinopsis](https://t.me/SINOPSIS_BTC)", "https://t.me/+PL2-eQPUhPg0Y2Ni"]



# test
channels_name = ["моча", "говно"]
channels_id = [-1001933170371, -1001998285090 ]
channels_link = ["[моча](https://t.me/testmylikedddd)", "https://t.me/cttssshh241"]

#меню
main_menu_buttons = [ 
    'Список игр',
   
    'Описание бота',
    'Партнерство и обратная связь'
    ]

def markup_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i = 0
    for menu_item in main_menu_buttons:
        item = types.KeyboardButton(menu_item)
        markup.row(item)
        i += 1
    return markup


games = [
    '<Назад',
    'Blum', 
    'Хомяки', 
    'Zavod',
    'PocketFi',
    'PixelTap',
    'Котики', 
    'Биттон', 
    'Хот', 
    'МТК', 
    'bcoin 2048',
    'cyber finance', 
    'memefi', 
    'vertus', 
    'fuel', 
    'Tapswap', 
    'Wave Wallet mining Ocean', 
     
    
    ]

def markup_games():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i = 0
    for game in games:
        item = types.KeyboardButton(game)
        markup.row(item)
        i += 1
    return markup


blum_buttons = [
    'Назад','Чат 🖤','Информация о проекте 🖤',
    '8 часов 🖤']

def blum_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in blum_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


humster_buttons = [
    'Назад','Чат 🐹','Информация о проекте 🐹',
    '3 часа 🐹']

def humster_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in humster_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


zavod_buttons = [
    'Назад','Чат 🏗️','Информация о проекте 🏗️',
    '3 часа 🏗️']

def zavod_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in zavod_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


pocketfi_buttons = [
    'Назад','Чат 📱','Информация о проекте 📱',
    '3 часа 📱']

def pocketfi_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in pocketfi_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


pixeltap_buttons = [
    'Назад','Чат 👾','Информация о проекте 👾',
    '3 часа 👾']

def pixeltap_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in pixeltap_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


cats_buttons = [
    'Назад','Чат 🐱','Информация о проекте 🐱',
    '3 часа 🐱']

def cats_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in cats_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


bitton_buttons = [
    'Назад','Чат 💼','Информация о проекте 💼',
    '3 часа 💼']

def bitton_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in bitton_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


hot_buttons = [
    'Назад','Чат 🔥','Информация о проекте 🔥',
    '2 часа 🔥', '3 часа 🔥', '4 часа 🔥', '5 часа 🔥', '6 часа 🔥']

def hot_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in hot_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


mtk_buttons = [
    'Назад','Чат 🏦','Информация о проекте 🏦',
    '3 часа 🏦']

def mtk_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in mtk_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


bcoin2048_buttons = [
    'Назад','Чат 🌚','Информация о проекте 🌚',
    '3 часа 🌚']

def bcoin2048_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in bcoin2048_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup









cyber_finance_buttons = [
    'Назад','Чат 🔨','Информация о проекте 🔨',
    '3 часа 🔨']

def cyber_finance_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in cyber_finance_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


memefi_buttons = [
    'Назад','Чат ⚔️','Информация о проекте ⚔️',
    '3 часа ⚔️']

def memefi_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in memefi_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


vertus_buttons = [
    'Назад','Чат 🍀','Информация о проекте 🍀',
    '3 часа 🍀']

def vertus_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in vertus_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


fuel_buttons = [
    'Назад','Чат 🅾️','Информация о проекте 🅾️',
    '3 часа 🅾️']

def fuel_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in fuel_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


tapswap_buttons = [
    'Назад','Чат 🌕','Информация о проекте 🌕',
    '3 часа 🌕']

def tapswap_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in tapswap_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup


wave_wallet_mining_ocean_buttons = [
    'Назад','Чат 🌴','Информация о проекте 🌴',
    '3 часа 🌴']

def wave_wallet_mining_ocean_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    i = 0
    for button in wave_wallet_mining_ocean_buttons:
        item = types.KeyboardButton(button)
        markup.row(item)
        i += 1
    return markup








