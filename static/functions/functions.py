import re
import pyttsx3
import platform
import sys
# import uuid
# import sqlite3

from datetime import datetime
from rich import print
from plyer import notification


# Config >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
args = sys.argv  # Get terminal arguments
argv = [

]
argv.append(args)


# Colors
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

plataforma = platform.system()

if 'Windows' in plataforma:
    # Bring leticia's voice function
    sara_voz = pyttsx3.init('sapi5')

    # Sara's voice adjustment function
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', voz[4].id)
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)

else:
    # Bring leticia's voice function. If it is not the standard leticia voice, it is Espeak.
    sara_voz = pyttsx3.init()

    # Sara's voice adjustment function
    sara_voz.setProperty('voice', 'pt+f2')
    # In 'm2' (male), you can put 'f2' (female) and numbers up to 7
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)


# Functions>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Speak, tell sara to say the sentences out loud>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*


def speak(audio):
    # notification.notify(title= "Sara", message = audio, app_name="SaraWA", app_icon="../img/sara_img.png", timeout=3, ticker="2", toast=True)
    # notification.notify(title = "SARA",message = audio,timeout = 3)

    # stream.stop_stream()

    if ('-U' in argv[0]):
        pass
    else:

        # audio = emoji.demojize(audio, delimiters=('', ''))

        audio = remove_emojis(audio)

        print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
        sara_voz.say(audio)
        sara_voz.runAndWait()

    # stream.start_stream ()


def speakUi(audio):
    # notification.notify(title= "Sara", message = audio, app_name="SaraWA", app_icon="../img/sara_img.png", timeout=3, ticker="2", toast=True)
    # notification.notify(title = "SARA",message = audio,timeout = 3)

    # stream.stop_stream()

    # print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
    sara_voz.say(audio)
    sara_voz.runAndWait()

# Say returns speech as a list for UI>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*


def say(args: list) -> str:
    if ('-U' in argv[0]):
        pass
    else:
        strings = [

        ]

        for i in args:
            speak(i)
            strings.append(i)

        return "\n".join(strings)


def show(args):
    if ('-U' in argv[0]):
        pass
    else:
        strings = [

        ]

        for i in args:
            strings.append(i)

        return '\n'.join(strings)

# Hour


def time_hour():

    hora = datetime.now()
    horas = hora.strftime('%H horas e %M minutos')
    speak(f'It is {horas}')


# Salva Historico
# -==-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-

# def salvar_conversa(pergunta, resposta):
#     # define o nome do arquivo a ser utilizado

#     # cria uma conexão com o banco de dados
#     conn = sqlite3.connect('chat.db')

#     # cria a tabela de mensagens se ela não existe
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS mensagens (
#             id TEXT PRIMARY KEY,
#             role TEXT,
#             content TEXT,
#             in_reply_to TEXT
#         )
#     ''')

#     # gera um ID único para a mensagem
#     id_mensagem = str(uuid.uuid4())

#     # insere a mensagem do usuário na tabela
#     conn.execute('''
#         INSERT INTO mensagens (id, role, content)
#         VALUES (?, ?, ?)
#     ''', (id_mensagem, 'user', pergunta))

#     # insere a mensagem do bot na tabela
#     conn.execute('''
#         INSERT INTO mensagens (id, role, content, in_reply_to)
#         VALUES (?, ?, ?, ?)
#     ''', (str(uuid.uuid4()), 'bot', resposta, id_mensagem))

#     # salva as mudanças no banco de dados
#     conn.commit()

#     # fecha a conexão com o banco de dados
#     conn.close()

#     print(f"Conversa salva com sucesso no banco de dados 'conversas.db'")


# # Obter histoico de conversas
# def obter_historico_de_conversas(db_path="chat.db", max_tokens_per_message=4000, max_messages=None, part_size=100):
#     # conecte-se ao banco de dados
#     conn = sqlite3.connect(db_path)
#     c = conn.cursor()

#     # obtenha todas as mensagens da tabela de mensagens
#     c.execute('SELECT content FROM mensagens WHERE role = "user"')
#     mensagens = [row[0] for row in c.fetchall()]

#     # divida as mensagens em pedaços menores
#     mensagens_divididas = []
#     for mensagem in mensagens:
#         while len(mensagem) > max_tokens_per_message:
#             mensagens_divididas.append(mensagem[:max_tokens_per_message])
#             mensagem = mensagem[max_tokens_per_message:]
#         mensagens_divididas.append(mensagem)

#     # divida as mensagens em partes menores
#     mensagens_partes = [mensagens_divididas[i:i+part_size]
#                         for i in range(0, len(mensagens_divididas), part_size)]

#     # limite o número de mensagens retornadas, se necessário
#     if max_messages is not None:
#         mensagens_partes = mensagens_partes[:max_messages]

#     # feche a conexão com o banco de dados
#     conn.close()

#     return mensagens_partes
