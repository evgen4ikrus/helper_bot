import logging
from environs import Env
from google.cloud import dialogflow
import json


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def create_intent(project_id, display_name, training_phrases_parts, message_text):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    message_text = [message_text]
    text = dialogflow.Intent.Message.Text(text=message_text)
    message = dialogflow.Intent.Message(text=text)
    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    logger.info("Intent created: {}".format(response))


def main() -> None:
    env = Env()
    env.read_env()
    project_id = env('PROJECT_ID')
    with open("new_intents.json", "r", encoding='UTF-8') as file:
        intents = json.loads(file.read())
    for display_name, intent in intents.items():
        create_intent(project_id, display_name, intent['questions'], intent['answer'])


if __name__ == '__main__':
    main()
