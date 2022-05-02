# Too Easy Travel - telegram bot v1.0
- _Дата релиза первой версии: 16.04.2022_ 
- Python 3.10.1
- [_Разработчик_](https://github.com/DaniilSh23)
___
##### Библиотеки для работы с ботом
1. re 
2. TelegramBotAPI 4.4.0
3. DateTime 4.4
4. python-telegram-bot-calendar 1.0.5
5. requests 2.27.1
6. json
7. sqlite3
8. loguru 0.6.0
___
#### Инструкция по установке
- Установить нужные модули
- Создать файл auth_data.py
- Создать две переменных с названием TOKEN и keyAPI
- Записываем в переменные выше токен телеграм бота и ключ от RapidAPI
- Запускаем бота командой **py main.py**
___
#### Используемые сервисы
- [Hotel](https://ru.hotels.com/)
- [RapidAPI](https://rapidapi.com/apidojo/api/hotels4/)
___
#### Описание команд
**Команда /lowprice** 
_После ввода команды у пользователя запрашивается:_
- Город, где будет проводиться поиск.
- Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума).
- Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)

**Команда /highprice**
_После ввода команды у пользователя запрашивается:_
- Город, где будет проводиться поиск.
- Количество отелей, которые необходимо вывести в результате (не больше
заранее определённого максимума).
- Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”)
- При положительном ответе пользователь также вводит количество
необходимых фотографий (не больше заранее определённого
максимума)

**Команда /bestdeal**
_После ввода команды у пользователя запрашивается:_
- Город, где будет проводиться поиск.
- Диапазон цен.
- Диапазон расстояния, на котором находится отель от центра.
- Количество отелей, которые необходимо вывести в результате (не больше
заранее определённого максимума).
- Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”)
- При положительном ответе пользователь также вводит количество
необходимых фотографий (не больше заранее определённого
максимума)

**Команда /history**
_После ввода команды пользователю выводится история поиска отелей. Сама история
содержит:_
- Команду, которую вводил пользователь.
- Дату и время ввода команды.
- Отели, которые были найдены.