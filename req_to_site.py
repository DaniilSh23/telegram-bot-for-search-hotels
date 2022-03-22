import json
import requests


def fst_request_for_destination_id(city: str):
    '''
    Функция запроса для получения id места назначения. Формирует json файл.

    :param city: str
            - город назначения
    :return: None
    '''

    querystring = {"query": city, "locale": "en_US", "currency": "USD"}
    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "257cce99f6mshfee5d9176fa2b7cp1ac4bcjsnd320e689ef14"
    }

    fst_req = requests.get('https://hotels4.p.rapidapi.com/locations/v2/search', headers=headers, params=querystring)
    fst_req_data = json.loads(fst_req.text)
    with open('fst_req.json', 'w') as fst_req_file:
        json.dump(fst_req_data, fst_req_file, indent=8)


def sec_request_for_hotel_info(destination_id: str, check_in: str = '2022-05-09', check_out: str = '2022-06-12'):
    '''
    Функция API запроса для получение полной информации об отелях с учётом параметров.
    Формирует json файл.

    :param destination_id: str
            - id места назначения
    :param check_in: str
            - дата заезда в формате год-месяц-дата
    :param check_out: str
            - дата выезда в формате год-месяц-дата
    :return: None
    '''

    querystring = {"destinationId": destination_id, "pageNumber": "1", "pageSize": "25", "checkIn": check_in,
                   "checkOut": check_out, "adults1": "1", "sortOrder": "PRICE", "locale": "en_US", "currency": "USD"}
    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "257cce99f6mshfee5d9176fa2b7cp1ac4bcjsnd320e689ef14"
    }

    sec_req = requests.get('https://hotels4.p.rapidapi.com/properties/list', headers=headers, params=querystring)
    sec_req_data = json.loads(sec_req.text)
    with open('sec_req.json', 'w') as sec_req_file:
        json.dump(sec_req_data, sec_req_file, indent=8)


def third_request_for_hotels_photo(hotel_id: str):
    '''
    Функция API запроса для получения фото отеля.
    Формирует json файл.

    :param hotel_id: id отеля
    :return: None
    '''

    querystring = {"id": hotel_id}
    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "257cce99f6mshfee5d9176fa2b7cp1ac4bcjsnd320e689ef14"
    }
    third_req = requests.get("https://hotels4.p.rapidapi.com/properties/get-hotel-photos", headers=headers, params=querystring)
    third_req_data = json.loads(third_req.text)
    with open('third_req.json', 'w') as third_req_file:
        json.dump(third_req_data, third_req_file, indent=8)
