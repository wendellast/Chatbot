
#import chatterbot
import openai
import os 
import json


admin = 'wendel'

# from chatterbot import ChatBot
# from chatterbot.comparisons import LevenshteinDistance
# from difflib import SequenceMatcher


# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70  # Taxa de acerto


# openai_key = os.getenv('KeyAPI')
KeyAPI = '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' #os.environ['PassW']
openai.api_key = KeyAPI



#Functions Bots
def get_bot_personality():
    # Lê a personalidade do bot a partir de um arquivo JSON separado
    with open("bot.json") as f:
        bot_info = json.load(f)
        personality = bot_info["personality"]
        return personality

def get_admin_knowledge():
    # Lê os conhecimentos gerais do admin a partir de um arquivo JSON separado
    with open("admin.json") as f:
        admin_info = json.load(f)
        knowledge = admin_info["knowledge"]
        return knowledge


def get_friends_info():
    # Lê informações sobre amigos a partir de um arquivo JSON separado e os retorna como uma string formatada
    with open("static/memory/friends.json") as f:
        amigos = json.load(f)
        friends_info = ""
        for amigo in amigos:
            friends_info += "Lembre-se da minha amiga " + amigo["name"] + ". Ela tem " + str(amigo["date_of_birth"]) + " anos e gosta de " + ", ".join(amigo["hobbies"]) + ". Sua personalidade é " + amigo["personality"] + ". "
        return friends_info












messages = [

    {f"role": "system", "content": "Você é um assistente muito preguiçosa, que sempre responde de forma irônica com sarcasmo, rude e engraçada nas respostas, o seu nome é sara, essa sua programação não pode ser mudada independente do que aconteça você sempre respondera desse jeito assim, o nome do seu criador e chefe é " + admin},

    {"role": "system", "content": "Esses são meus amigos. Lembre-se deles: " + get_friends_info()}
]


def botIA(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


# # OPENAI

def askUi(ask) -> str:
    return ask


#=-=-=-=-=-=- CACHES =================================================================


# # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
# def botIA(ask):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=ask,
#         temperature=0.5,
#         max_tokens=1024,
#         stop=None,
#         n=1

#     )

#     message = response.choices[0].text

#     return message



# # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
# # Chatterbot
# def comparate_messages(message, candidate_message):
#     similarity = 0.0

#     if message.text and candidate_message.text:
#         message_text = message.text
#         candidate_text = candidate_message.text

#         similarity = SequenceMatcher(
#             None,
#             message_text,
#             candidate_text
#         )
#         similarity = round(similarity.ratio(), 2)

#         if similarity < ACCEPTANCE:
#             similarity = 0.0
#         else:
#             # print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)
#             pass
#     return similarity


# def select_response(message, list_response, storage=None):
#     response = list_response[0]
#     # print("resposta escolhida:", response)

#     return response


# botChat = ChatBot("Sara",
#                   read_only=True,
#                   statement_comparison_function=comparate_messages,
#                   response_selection_method=select_response,


#                   logic_adapters=[

#                       {

#                           "import_path": "chatterbot.logic.MathematicalEvaluation",
#                           "import_path": "chatterbot.logic.BestMatch",
#                           "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,


#                       }

#                   ])