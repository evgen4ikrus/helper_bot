# helper_bot

## Установка
Для работы скрипта вам понадобится Python третьей версии.

* Скачайте код с GitHub.
* Установите зависимости:
```sh
pip install -r requirements.txt
```
* Создайте [Google-проект](https://cloud.google.com/dialogflow/es/docs/quick/setup) и [агента в DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).
* Запишите переменные окружения в файле .env в формате КЛЮЧ=ЗНАЧЕНИЕ:
`GOOGLE_APPLICATION_CREDENTIALS` - путь до файла с JSON-ключом. [Получить ключ](https://cloud.google.com/docs/authentication/client-libraries).

`PROJECT_ID` - ID Google проекта.

TELEGRAM_API_TOKEN - Токен Телеграмма. Получить можно у [BotFather](https://telegram.me/BotFather).
## Запуск
Запустите скрипт командой:
```
python bot.py
```
