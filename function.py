import datetime


def date_adress():
    day_number = datetime.date.today().strftime("%j")
    return f'🍀 Сегодня наш актуальный адрес: http://zenitnow{int(day_number)-112}.top. Удачных ставок! 🍀'


def promotions_adress():
    day_number = datetime.date.today().strftime("%j")
    return f'🎊 Акции и розыгрыши - вот здесь: http://zenitnow{int(day_number)-112}.top/promotions. Все получится! 🎊'


def android_application_adress():
    day_number = datetime.date.today().strftime("%j")
    return f'📱 Скачать приложение можно по ссылке: http://zenitnow{int(day_number)-112}.top/ru/mobile_app/android. Оно крутое, правда! 📱'


def ios_application_adress():
    day_number = datetime.date.today().strftime("%j")
    return f'📱 Скачать приложение можно по ссылке: http://zenitnow{int(day_number)-112}.top/ru/application/ios. Оно крутое, правда! 📱'