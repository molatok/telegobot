from aiogram import types, Dispatcher
from function import date_adress, promotions_adress, android_application_adress, ios_application_adress
from Key.keyboard import keyboard
from bot_start import bot


async def process_start_command(message: types.Message):
    await message.answer(f'Привет! Это бот БК Zenit. Выбери, пожалуйста, пункт меню на клавиатуре ниже, чтобы узнать '
                         f'о нас больше:',
                         reply_markup=keyboard)


async def process_keyboard_command(message: types.Message):
    await message.answer(f'{date_adress()}')


async def process_test_command(message: types.Message):
    await message.answer(f'{promotions_adress()}')


async def process_vk_command(message: types.Message):
    await message.answer(f'Подписывайтесь на нашу группу: https://vk.com/zenitbetofficial')


async def process_instagram_command(message: types.Message):
    await message.answer(f'Подписывайтесь на нашу страницу: https://www.instagram.com/zenitbetcom/')


async def process_tg_command(message: types.Message):
    await message.answer(f'Подписывайтесь на наш паблик: https://t.me/zenit_bet_bk')


async def process_support_command(message: types.Message):
    await message.answer(f'Уже ищу для тебя лучшего оператора :) А пока - опиши свой вопрос:')


async def process_ios_command(message: types.Message):
    await message.answer(f'{ios_application_adress()}')


async def process_android_command(message: types.Message):
    await message.answer(f'{android_application_adress()}')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_test_command, text='Акции')
    dp.register_message_handler(process_keyboard_command, text='Адрес сайта')
    dp.register_message_handler(process_vk_command, text='Вконтакте')
    dp.register_message_handler(process_instagram_command, text='instagram')
    dp.register_message_handler(process_tg_command, text='Telegram')
    dp.register_message_handler(process_support_command, text='Поддержка')
    dp.register_message_handler(process_ios_command, text='приложение iOS')
    dp.register_message_handler(process_android_command, text='приложение Android')
