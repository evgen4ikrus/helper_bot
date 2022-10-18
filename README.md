# helper_bot
Бот помошник для распознавания речи для VK и Telegram.
## Примеры работы ботов:
[Работающий бот](https://t.me/TestDevmanBot) в Telegram.

Пример результата для Telegram:

![tg](https://dvmn.org/media/filer_public/7a/08/7a087983-bddd-40a3-b927-a43fb0d2f906/demo_tg_bot.gif)

[Работающий бот](https://vk.com/im?sel=-216519868) в группе VK.

Пример результата для VK:

![vk](https://dvmn.org/media/filer_public/1e/f6/1ef61183-56ad-4094-b3d0-21800bdb8b09/demo_vk_bot.gif)
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

`TELEGRAM_TOKEN` - Токен Телеграмма. Получить можно у [BotFather](https://telegram.me/BotFather).

`VK_GROUP_TOKEN` - Токер группы VK. Получить в настройках группы, в меню “Работа с API”.

`TELEGRAM_CHAT_ID` - ID чата в телеграм, в который будут приходить логи.
## Скрипты:
### tg_bot.py
Запускает телеграмм бота.

Запуск:
```
python tg_bot.py
```
### vk_bot.py
Запускает бота в группе VK.

Запуск:
```
python vk_bot.py
```
### create_intents.py
Создает Intent на [DialogFlow](https://dialogflow.cloud.google.com/) из данных json-файла.

Создайте файл `new_intent.json` с содержимым, которое имеет вид:
``` python
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Вопросы от действующих партнёров": {
        "questions": [
            "Где проходит совещание",
            "Когда переведёте деньги по контракту",
            "Скоро переведу деньги по контракту",
            "Задерживаемся на совещание",
            "Высылаю итоги совещания",
            "Когда подписываем контракт?",
            "Контракт уже в силе?"
        ],
        "answer": "Простите, в этом чате сидит SMM-отдел, мы не знаем ответа на этот вопрос. Обратитесь напрямую к сотруднику, с которым работаете."
    }
}
```
Запустите скрипт:
```
python create_intent.py
```
