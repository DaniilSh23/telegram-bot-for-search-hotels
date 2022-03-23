import json


def destination_id():
    ''' В функции получаем id места назначения '''

    with open('fst_req.json', 'r') as fst_req_file:
        fst_req_file = json.load(fst_req_file)
    return fst_req_file['suggestions'][0]['entities'][0]['destinationId']


def result_of_search_hotels():
    ''' В sec_req.json лежит информация об отелях.
    В функции получаем список с результатами поиска отелей '''

    with open('sec_req.json', 'r') as sec_req_file:
        work_file = json.load(sec_req_file)
    return list(work_file['data']['body']['searchResults']['results'])


def print_hotel_photo(num_hot_photo):
    ''' Функция, которая из json файла формирует список с информацией о фото отеля. '''

    with open('third_req.json', 'r') as third_req_file:
        work_file = json.load(third_req_file)
        hot_photo_lst = work_file['hotelImages']
        try:
            photo_url_lst = []
            for i_num in range(num_hot_photo):
                hot_photo_url = hot_photo_lst[i_num]['baseUrl'].format(size='y')
                photo_url_lst.append(hot_photo_url)
            return photo_url_lst
        except IndexError:
            photo_url_lst.append('Увы, но столько фото отеля нет...')
            return photo_url_lst



