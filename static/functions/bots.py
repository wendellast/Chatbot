import chatterbot
import openai
import os 


from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from difflib import SequenceMatcher


# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70  # Taxa de acerto


# openai_key = os.getenv('KeyAPI')
KeyAPI = '22' #os.environ['PassW']
openai.api_key = KeyAPI


# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
# Chatterbot
def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(
            None,
            message_text,
            candidate_text
        )
        similarity = round(similarity.ratio(), 2)

        if similarity < ACCEPTANCE:
            similarity = 0.0
        else:
            # print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)
            pass
    return similarity


def select_response(message, list_response, storage=None):
    response = list_response[0]
    # print("resposta escolhida:", response)

    return response


botChat = ChatBot("Sara",
                  read_only=True,
                  statement_comparison_function=comparate_messages,
                  response_selection_method=select_response,


                  logic_adapters=[

                      {

                          "import_path": "chatterbot.logic.MathematicalEvaluation",
                          "import_path": "chatterbot.logic.BestMatch",
                          "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,


                      }

                  ])


# OPENAI
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def botIA(ask):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=ask,
        temperature=0.5,
        max_tokens=1024,
        stop=None,
        n=1

    )

    message = response.choices[0].text

    return message


def askUi(ask) -> str:
    return ask
