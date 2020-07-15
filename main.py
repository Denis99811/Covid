import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()

bot = telebot.TeleBot('1282414951:AAE0RVGltHcxgxtvHyimL31rXYLo1ECLrLg')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('/countries')
    btn2 = types.KeyboardButton('/help')
    markup.add(btn1, btn2)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные по Коронавирусу в определенной стране, выберите пункт '/countries'"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('/countries')
    markup.add(btn1)

    send_message = f"Данный тестовый бот предназначен для мониторинга статистики больных и умерших коронавирусом в странах и во всем мире. Для того, чтобы посмотреть, какие страны включены в статистику, нажмите на кнопку 'Список стран'.\n" \
                    f"Бот поддерживает такие стандартные команды, как /start, /help\n" \
                    f"Чтобы проверить бота, нужно выбрать определенную страну(необходимо ввести команду /countries), в которой вы хотите посмотреть статистику заражения коронавирусом или же написать боту название страны\n" \
                    f"<b>Если же вы ввели неправильное название страны или ввели команду, которую бот не понимает, то он выдаст данные заражения коронавирусом по всему миру.</b>"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
        
@bot.message_handler(commands=['countries'])
def countires(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('США')
    btn5 = types.KeyboardButton('Беларусь')
    btn6 = types.KeyboardButton('Казахстан')
    btn7 = types.KeyboardButton('Италия')
    btn8 = types.KeyboardButton('Франция')
    btn9 = types.KeyboardButton('Германия')
    btn10 = types.KeyboardButton('Япония')
    btn11 = types.KeyboardButton('Тайланд')
    btn12 = types.KeyboardButton('Бразилия')
    btn13 = types.KeyboardButton('Афганистан')
    btn14 = types.KeyboardButton('Колумбия')
    btn15 = types.KeyboardButton('Сербия')
    btn16 = types.KeyboardButton('Швеция')
    btn17 = types.KeyboardButton('Чили')
    btn18 = types.KeyboardButton('Мексика')
    btn19 = types.KeyboardButton('Испания')
    btn20 = types.KeyboardButton('Австралия')
    btn21 = types.KeyboardButton('Индия')
    btn22 = types.KeyboardButton('Перу')
    btn23 = types.KeyboardButton('Канада')


    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные по Коронавирусу выберите или напишите название страны из предложенных."
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip()
    if get_message_bot == "США":
    	location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "Украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "Россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "Беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "Казахстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "Италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "Франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "Германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "Япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "Тайланд":
        location = covid19.getLocationByCountryCode("TH")
    elif get_message_bot == "Бразилия":
        location = covid19.getLocationByCountryCode("BR")
    elif get_message_bot == "Афганистан":
        location = covid19.getLocationByCountryCode("AF")
    elif get_message_bot == "Колумбия":
        location = covid19.getLocationByCountryCode("CO")
    elif get_message_bot == "Сербия":
        location = covid19.getLocationByCountryCode("RS")
    elif get_message_bot == "Швеция":
        location = covid19.getLocationByCountryCode("SE")
    elif get_message_bot == "Чили":
        location = covid19.getLocationByCountryCode("CL")
    elif get_message_bot == "Мексика":
        location = covid19.getLocationByCountryCode("MX")
    elif get_message_bot == "Испания":
        location = covid19.getLocationByCountryCode("ES")
    elif get_message_bot == "Австралия":
        location = covid19.getLocationByCountryCode("AU")
    elif get_message_bot == "Индия":
        location = covid19.getLocationByCountryCode("IN")
    elif get_message_bot == "Перу":
        location = covid19.getLocationByCountryCode("PE")
    elif get_message_bot == "Канада":
        location = covid19.getLocationByCountryCode("CA")
    elif get_message_bot == "Во всём мире":
        location = covid19.getLatest()
        final_message =f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Смертей: </b>{location['deaths']:,}"
    else:
        location = covid19.getLatest()
        final_message = f"Бот не поддерживает страну/введенную команду.\nВведите /help для справки\n<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Смертей: </b>{location['deaths']:,}"
    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

        
bot.polling(none_stop=True)