import logging
from functools import partial

from environs import Env
from google.cloud import dialogflow
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(f'Здравствуйте, {user.mention_markdown_v2()}')


def reply_to_message(update: Update, context: CallbackContext, project_id) -> None:
    text = update.message.text
    session_id = str(update.effective_user.id)
    answer = detect_intent_texts(project_id, session_id, text, 'ru')
    update.message.reply_text(answer)


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response.query_result.fulfillment_text


def main() -> None:
    env = Env()
    env.read_env()
    telegram_token = env('TELEGRAM_TOKEN')
    updater = Updater(telegram_token)
    project_id = env('PROJECT_ID')

    dispatcher = updater.dispatcher

    reply_to_message_with_args = partial(reply_to_message, project_id=project_id)
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message_with_args))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
