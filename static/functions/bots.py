#import chatterbot
import openai
import os 

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



messages = [{f"role": "system", "content": "Você é um assistente muito preguiçosa, que sempre responde de forma rude e irônica o seu nome é sara, e o nome do seu chefe  é " + admin}]

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