## О проекте

* Этот проект - это простой набор скриптов на Python для удаленного управления включением и выключением компьютера через Telegram-бота.

## Возможности

* Включение компьютера через Telegram-бота.
* Выключение компьютера через Telegram-бота.
* Получение статуса компьютера через Telegram-бота.
## Установка и настройка

* Установите Python 3.8 или выше.
* Клонируйте репозиторий проекта на оба компьютера: на тот, который будет включаться и выключаться, и на тот, который будет постоянно включен.
* Установите необходимые библиотеки на оба компьютера, запустив следующую команду в командной строке
```
pip install python-telegram-bot wakeonlan python-dotenv
```
* Настройте параметры в файле .env на сервере (постоянно включенный компьютер). Для этого используйте файл .env.example как образец.
* Вставьте правильные значения в скрипт put_me_to_scheduler.vbs, заменив path_to_your_script на реальный путь к client.pyw на клиентском компьютере.
* Поместите скрипт put_me_to_scheduler.vbs в папку shell:startup на клиентском компьютере.
* Запустите server.py на сервере.
* Все готово! Вы теперь можете управлять вашим компьютером через Telegram-бота.