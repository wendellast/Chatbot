import openai
import json

# Config and vars
# * =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70  # Success rate

# openai_key = os.getenv('KeyAPI')
KeyAPI = 'Your key'  # os.environ['PassW']
openai.api_key = KeyAPI


# Functions Bots Protocolo

def get_admin_knowledge():
    # Reads the admin's general knowledge from a separate JSON file
    with open("static/memory/admin.json") as f:
        admin_info = json.load(f)
        admin = admin_info["admin"]
        return str(admin)


def get_description():
    # description
    with open("static/memory/description.json") as f:
        description_info = json.load(f)
        description = description_info["description"]
        return str(description)


def get_bot_personality():
    # Reads the bot's personality from a separate JSON file
    with open("static/memory/personality.json") as f:
        bot_info = json.load(f)
        personality = bot_info["personality"]
        return str(personality)


def get_bot_rules():
    # Reads the bot's rules from a separate JSON file
    with open("static/memory/rules.json") as f:
        bot_info = json.load(f)
        rules = bot_info["rules"]
        return str(rules)


def get_bot_mode():
    # Reads the bot's mode from a separate JSON file
    with open("static/memory/mode.json") as f:
        bot_info = json.load(f)
        mode = bot_info["mode"]
        return str(mode)


def get_bot_user():
    # Reads the bot's user from a separate JSON file
    with open("static/memory/user.json") as f:
        bot_info = json.load(f)
        user = bot_info["user"]
        return str(user)


def get_bot_memory():
    # Reads the admin's general knowledge from a separate JSON file
    with open("static/memory/memory.json", encoding='utf-8') as f:
        memory_info = json.load(f)
        memory = memory_info["messages"]
        return str(memory)


def get_family_info():
    # Reads information about friends from a separate JSON file and returns it as a formatted string
    with open("static/memory/family.json") as f:
        family = json.load(f)
        family_info = ""
        for relative in family:
            family_info += "Remember my " + relative["kinship"] + " " + relative["name"] + ". They are " + str(
                relative["date_of_birth"]) + " years old and like " + ", ".join(relative["hobbies"]) + ". Their personality is " + relative["personality"] + " and they are " + relative['gender'] + ". "
        return family_info


def get_friends_info():
    # Reads information about friends from a separate JSON file and returns it as a formatted string
    with open("static/memory/friends.json") as f:
        friends = json.load(f)
        friends_info = ""
        for friend in friends:
            friends_info += "Remember my friend " + friend["name"] + ". They are " + str(friend["date_of_birth"]) + " years old and like " + ", ".join(
                friend["hobbies"]) + ". Their personality is " + friend["personality"] + " and they are " + friend["gender"] + ". "
        return friends_info


# conversations = str(obter_historico_de_conversas())


# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*


messages = [

    {f"role": "system", "content": "Attention, this is your function protocol and what you should do. Listen carefully and pay close attention."},

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


    {"role": "system", "content": "This is your description, information about yourself: " + get_description()},

    {"role": "system", "content": "This is your personality, how you should act, speak, respond, etc. Always obey, do not break the protocol: " + get_bot_personality()},


    {"role": "system", "content": "These are your rules and behaviors. Follow everything correctly: " + get_bot_rules()},

    # {"role": "system", "content":"This is the message history of your creator. You must analyze the history to remember what was said before and learn and improve your questions and responses. Pay close attention to the data and always remember it: " + conversations},



    {"role": "system", "content": "This is your protocol regarding yourself and user information. Always follow the protocol and never break it, no matter what happens."},
]


def botIA(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


# # OPENAI

def askUi(ask) -> str:
    return ask
