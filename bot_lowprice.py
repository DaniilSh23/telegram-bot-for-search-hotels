import telebot
from auth_data import TOKEN
from datetime import datetime
import req_to_site
import defination_base_info


bot = telebot.TeleBot(f'{TOKEN}', parse_mode=None)
user_input_dct = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет. С тобой лучший чат-бот по поиску отелей и вот, что я умею: \n'
                          '/help - помощь по командам бота\n'
                          '/lowprice - вывод самых дешёвых отелей в городе\n'
                          '/highprice - вывод самых дорогих отелей в городе\n'
                          '/bestdeal - вывод отелей, наиболее подходящих по цене и расположению от центра\n'
                          '/history - вывод истории поиска отелей.')


@bot.message_handler(commands='lowprice')
def send_lowprice(message):
    city = 'Введите город поиска: '
    bot.send_message(message.chat.id, city)
    bot.register_next_step_handler(message, city_reg)


def city_reg(message):
    print('its city_reg')
    user_input_dct['city'] = message.text
    check_in = 'Введите дату заезда в формате (ГГГГ-ММ-ДД): '
    bot.send_message(message.chat.id, check_in)
    bot.register_next_step_handler(message, check_in_f)


def check_in_f(message):
    print('its check_in_f')
    user_input_dct['check_in'] = message.text
    check_out = 'Введите дату выезда в формате (ГГГГ-ММ-ДД): '
    bot.send_message(message.chat.id, check_out)
    bot.register_next_step_handler(message, check_out_f)

def check_out_f(message):
    print('its check_out_f')
    user_input_dct['check_out'] = message.text
    date_check_in = datetime.strptime(user_input_dct['check_in'], '%Y-%m-%d')
    date_check_out = datetime.strptime(user_input_dct['check_out'], '%Y-%m-%d')
    user_input_dct['date_difference'] = (date_check_out - date_check_in).days

    num_hotels = 'Сколько вывести отелей (лимит: 15 отелей): '
    bot.send_message(message.chat.id, num_hotels)
    bot.register_next_step_handler(message, num_hotels_f)

def num_hotels_f(message):
    print('its num_hotels_f')
    if int(message.text) > 15:
        bot.send_message(message.chat.id, 'Слишком много отелей...Я выведу 15 :)')
        user_input_dct['num_hotels'] = 15
    else:
        user_input_dct['num_hotels'] = int(message.text)
    send_photo = 'Будем загружать фото каждого отеля? (Да/Нет): '
    bot.send_message(message.chat.id, send_photo)
    bot.register_next_step_handler(message, send_photo_f)


def send_photo_f(message):
    print('its send_photo_f')
    if message.text.lower() == 'да':
        user_input_dct['send_photo'] = True
        num_hot_photo = 'Введите количество фото отеля (лимит: 15 фото): '
        bot.send_message(message.chat.id, num_hot_photo)
        bot.register_next_step_handler(message, num_hot_photo_f)
        print('мы вот после ')


def num_hot_photo_f(message):
    print('its num_hot_photo_f')
    if int(message.text) > 15:
        bot.send_message(message.chat.id, 'Слишком много фото...Я выведу 15 :)')
        user_input_dct['num_hot_photo'] = 15
    else:
        user_input_dct['num_hot_photo'] = int(message.text)
        req_and_answer(message)


def req_and_answer(message):
    req_to_site.fst_request_for_destination_id(user_input_dct['city'])
    destination_id = defination_base_info.destination_id()
    req_to_site.sec_request_for_hotel_info(destination_id=destination_id, check_in=user_input_dct['check_in'], check_out=user_input_dct['check_out'])

    hotels_lst = defination_base_info.result_of_search_hotels()
    hotels_lst = sorted(hotels_lst, key=lambda i_hotel: i_hotel['ratePlan']['price']['current'])
    print_info(message, hotels_lst)


def print_info(message, hotels_lst):
    for i_num in range(user_input_dct['num_hotels']):
        bot.send_message(message.chat.id, f'====={i_num + 1} ОТЕЛЬ=====')
        bot.send_message(message.chat.id, f'\nНазвание отеля: {hotels_lst[i_num]["name"]}\n'
              f'Рейтинг отеля: {hotels_lst[i_num]["starRating"]} звёзд\n'
              f'Адрес отеля: {hotels_lst[i_num]["address"]["streetAddress"]}, {hotels_lst[i_num]["address"]["locality"]}, '
              f'{hotels_lst[i_num]["address"]["postalCode"]}, {hotels_lst[i_num]["address"]["region"]}, {hotels_lst[i_num]["address"]["countryName"]}\n'
              f'Расстояние до центра города: {hotels_lst[i_num]["landmarks"][0]["distance"]}\n'
              f'Средняя цена за сутки: {hotels_lst[i_num]["ratePlan"]["price"]["current"]}\n'
              f'Суммарная стоимость проживания за {user_input_dct["date_difference"]} дня: {int(hotels_lst[i_num]["ratePlan"]["price"]["exactCurrent"]) * user_input_dct["date_difference"]}$\n'
              f'URL адрес отеля: {hotels_lst[i_num]["urls"]}\n')
        if user_input_dct['send_photo']:
            req_to_site.third_request_for_hotels_photo(hotel_id=hotels_lst[i_num]['id'])
            photo_url_lst = defination_base_info.print_hotel_photo(num_hot_photo=user_input_dct['num_hot_photo'])
            for i_photo_url in photo_url_lst:
                bot.send_message(message.chat.id, i_photo_url)
    else:
        bot.send_message(message.chat.id, 'Вот, собственно, и Ваш результат. Хорошего отдыха :)')


bot.infinity_polling()