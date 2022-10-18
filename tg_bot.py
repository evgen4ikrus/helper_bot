import logging
from functools import partial

import telegram
from environs import Env
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

from helpers import TelegramLogsHandler, detect_intent_texts

logger = logging.getLogger('tg_bot')


def start(update: telegram.Update, context: CallbackContext) -> None:
    update.message.reply_markdown_v2('Здравствуйте, чем можем помочь?')


def reply_to_message(update: telegram.Update, context: CallbackContext, project_id) -> None:
    text = update.message.text
    session_id = str(update.effective_user.id)
    answer = detect_intent_texts(project_id, session_id, text, 'ru')
    update.message.reply_text(answer)


def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    env = Env()
    env.read_env()
    telegram_token = env('TELEGRAM_TOKEN')
    project_id = env('PROJECT_ID')
    telegram_chat_id = env('TELEGRAM_CHAT_ID')

    bot = telegram.Bot(token=telegram_token)
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(bot, telegram_chat_id))
    logger.info('Бот для логов запущен')

    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher

    while True:

        try:
            reply_to_message_with_args = partial(reply_to_message, project_id=project_id)
            dispatcher.add_handler(CommandHandler('start', start))
            dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message_with_args))

            updater.start_polling()
            logger.info('Telegram bot запущен')
            updater.idle()

        except Exception:
            logger.exception('Произошла ошибка:')


if __name__ == '__main__':
    main()
