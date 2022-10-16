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
## Скрипты:
### tg_bot.py
Запускает телеграмм бота

Запуск:
```
python tg_bot.py
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