from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

key1 = KeyboardButton('Адрес сайта')
key2 = KeyboardButton('Акции')
key3 = KeyboardButton('Вконтакте')
key4 = KeyboardButton('Telegram')
key5 = KeyboardButton('instagram')
key6 = KeyboardButton('Поддержка')
key7 = KeyboardButton('приложение iOS')
key8 = KeyboardButton('приложение Android')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(key1).insert(key2).add(key3).insert(key4).insert(key5).add(key6).add(key7).insert(key8)