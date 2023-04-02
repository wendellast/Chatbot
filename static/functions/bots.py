#import chatterbot
import openai
import json
from static.functions.functions import obter_historico_de_conversas


# from chatterbot import ChatBot
# from chatterbot.comparisons import LevenshteinDistance
# from difflib import SequenceMatcher


# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70  # Taxa de acerto


# openai_key = os.getenv('KeyAPI')
KeyAPI = 'Seu key' #os.environ['PassW']
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
        
    
def get_bot_mode():
    # Lê a personalidade do bot a partir de um arquivo JSON separado
    with open("static/memory/mode.json") as f:
        bot_info = json.load(f)
        mode  = bot_info["mode"]
        return str(mode)
    
def get_bot_user():
    # Lê a personalidade do bot a partir de um arquivo JSON separado
    with open("static/memory/user.json") as f:
        bot_info = json.load(f)
        user  = bot_info["user"]
        return str(user)
    
def get_bot_memory():
    # Lê os conhecimentos gerais do admin a partir de um arquivo JSON separado
    with open("static/memory/memory.json", encoding='utf-8') as f :
        memory_info = json.load(f)
        memory = memory_info["mensagens"]
        return str(memory)


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


conversas = str(obter_historico_de_conversas())


# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*



messages= [

{f"role": "system", "content": "Atenção esse é o seu protocolo de funções e como você e o que deve fazer, esculte bem e preste muita atenção "},

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


{"role": "system", "content":"Essa é sua descrição suas informações sobre você " + get_description()},

{"role": "system", "content":"Essa é sua personalidade como você deve agir, falar, responder etc obedeça sempre não quebre o protocolo" +  get_bot_personality()},


{"role": "system", "content":"Essa São as regras e comportamento seu siga tudo certinho " +  get_bot_rules()},

# {"role": "system", "content":"Esse o é o histórico de messages do seu criador, você deve analisar o histórico para lembrar do que foi dito antes, e aprender e melhorar suas perguntas e resposta, preste muita atenção nos dados ai e lembre-se sempre deles: " + conversas},



{"role": "system", "content":"Esse é o seu protocolo sobre  você e as informações do usuário, deve sempre seguir o protocolo e nunca quebra-lo independente do que aconteça"},
]





def botIA(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply




# # OPENAI

def askUi(ask) -> str:
    return ask

