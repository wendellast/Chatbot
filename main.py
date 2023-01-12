import datetime
from rich import print
from static.functions.bots import *
from static.functions.functions import *

#Main >>> 
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def bot_resp(ask):
    ask = ask.lower()

    # Resposta do Sistema
    if ('bom dia' in ask):  # Boa Noite Sara
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            fale('Olá')
            fale('Bom dia')

        elif Horario >= 12 and Horario < 18:
            fale('Agora não é mais de manhã')
            fale('Já passou do meio dia')
            fale('Estamos no período da tarde')

        elif Horario >= 18 and Horario != 0:
            fale('Agora não é de manhã')
            fale('Já estamos no período noturno')
            fale('Boa noite')

    else:

        # Resposta Chatterbot
        response = botChat.get_response(ask)

        if response.confidence > 0.0:
            print(response.text)
            return response.text

        # Resposta OpenAI
        else:
            resp1 = botIA(ask)
            print(resp1)
            return resp1
