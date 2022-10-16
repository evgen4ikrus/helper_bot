import logging
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger("vk bot")


def main() -> None:
    env = Env()
    env.read_env()
    vk_group_token = env('VK_GROUP_TOKEN')
    vk_session = vk_api.VkApi(token=vk_group_token)
    longpoll = VkLongPoll(vk_session)
    logger.info('VK bot запущен')

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            if event.to_me:
                print('Для меня от: ', event.user_id)
            else:
                print('От меня для: ', event.user_id)
            print('Текст:', event.text)


if __name__ == '__main__':
    main()
