import logging
import random

import telegram
import vk_api as vk
from environs import Env
from vk_api.longpoll import VkEventType, VkLongPoll

from dialogflow_helpers import detect_intent_texts
from log_helpers import TelegramLogsHandler

logger = logging.getLogger('vk_bot')


def reply_to_message(event, vk_api, project_id):
    session_id = event.user_id
    answer = detect_intent_texts(project_id, session_id, event.text, 'ru', fallback_accounting=False)
    if answer:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    env = Env()
    env.read_env()
    telegram_token = env('TELEGRAM_TOKEN')
    telegram_chat_id = env('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=telegram_token)
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(bot, telegram_chat_id))
    logger.info('Бот для логов запущен')

    project_id = env('PROJECT_ID')
    vk_group_token = env('VK_GROUP_TOKEN')
    vk_session = vk.VkApi(token=vk_group_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    logger.info('VK bot запущен')

    while True:

        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    reply_to_message(event, vk_api, project_id)

        except Exception:
            logger.exception('Произошла ошибка:')


if __name__ == '__main__':
    main()
