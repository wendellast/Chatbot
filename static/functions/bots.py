
#import chatterbot
import openai
import os 
import json



# from chatterbot import ChatBot
# from chatterbot.comparisons import LevenshteinDistance
# from difflib import SequenceMatcher


# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70  # Taxa de acerto


# openai_key = os.getenv('KeyAPI')
KeyAPI = 'sua key' #os.environ['PassW']
openai.api_key = KeyAPI



#Functions Bots Protocolo

def get_admin_knowledge():
    # Lê os conhecimentos gerais do admin a partir de um arquivo JSON separado
    with open("static/memory/admin.json") as f:
        admin_info = json.load(f)
        admin = admin_info["admin"]
        return str(admin)


def get_description():
    #descrição
    with open("static/memory/description.json") as f:
        description_info = json.load(f)
        description = description_info["description"]
        return str(description)

def get_bot_personality():
    # Lê a personalidade do bot a partir de um arquivo JSON separado
    with open("static/memory/personality.json") as f:
        bot_info = json.load(f)
        personality = bot_info["personality"]
        return str(personality)
    
def get_bot_rules():
    # Lê a personalidade do bot a partir de um arquivo JSON separado
    with open("static/memory/rules.json") as f:
        bot_info = json.load(f)
        rules  = bot_info["rules"]
        return str(rules)

def get_family_info():
    # Lê informações sobre amigos a partir de um arquivo JSON separado e os retorna como uma string formatada
    with open("static/memory/family.json") as f:
        familia = json.load(f)
        family_info = ""
        for parente in familia:
            family_info += "Lembre-se da minha do meu parente " + parente["kinship"] + "o nome dele é" + parente["name"] + ". Ela tem " + str(parente["date_of_birth"]) + " anos e gosta de " + ", ".join(parente["hobbies"]) + ". Sua personalidade é " + parente["personality"] + "O seu sexo é "+ parente['gender'] +". "
        return family_info


def get_friends_info():
    # Lê informações sobre amigos a partir de um arquivo JSON separado e os retorna como uma string formatada
    with open("static/memory/friends.json") as f:
        amigos = json.load(f)
        friends_info = ""
        for amigo in amigos:
            friends_info += "Lembre-se da minha amiga " + amigo["name"] + ". Ela tem " + str(amigo["date_of_birth"]) + " anos e gosta de " + ", ".join(amigo["hobbies"]) + ". Sua personalidade é " + amigo["personality"] + "o seu sexo é"+ amigo["gender"]+ ". "
        return friends_info




# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
messages = [

    {f"role": "system", "content": "ATENÇÃO A PARTE DE AGORA QUANDO EU DICER 'INICIAR TREINAMENTO', ESCULTE COM ATENÇÃO TUDO O QUE VOU DIZER POIS ESSE SERA O SEU PROTOCOLO E NÃO PODERÁ SER QUEBRADO. ASSIM QUE EU DICER 'TREINAMENTO TERMINADO' JÁ PODE conversar e responder ao usuário "},

    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    {"role": "system", "content":"INICIAR TREINAMENTO"},

    {"role": "system", "content":"Essas são as informações do seu chefe criador admin, lembre sempre de obedece-lo" + get_admin_knowledge()},

    {"role": "system", "content":"Essa é sua descrição suas informações sobre você " + get_description()},

    {"role": "system", "content":"Essa é sua personalidade como você deve agir, falar, responder etc obedeça sempre não quebre o protocolo" +  get_bot_personality()},

    
    {"role": "system", "content":"Essa São as regras e comportamento seu siga tudo certinho " +  get_bot_rules()},

    {"role": "system", "content": "Esses são meus amigos. Lembre-se deles sempre que o usuário perguntar você tem autorização para fazer sobre eles.: " + get_friends_info()},

    {"role": "system", "content": "Esses são minha familia. Lembre-se deles  sempre que o usuário perguntar você tem autorização para fazer sobre ele:" + get_family_info()},

    {"role": "system", "content":"Esse é o seu protocolo sobre  você e as informações do usuário, deve sempre seguir o protocolo e nunca quebra-lo independente do que aconteça"},

    {"role": "system", "content":"TREINAMENTO TERMINADO"},


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