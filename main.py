import datetime

from train_sara import treinar
from rich import print
from static.functions.bots import *
from static.functions.functions import *


# Main >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def bot_resp(ask):
    ask = ask.lower()
    Horario = int(datetime.datetime.now().hour)

    # Resposta do Sistema
    if ('bom dia' in ask):

        if (Horario >= 0 and Horario < 12):

            phrases = [
                'Bom dia !'
                'Espero que tenha uma ótima manhã'

            ]

            reps = say(phrases)

            return reps

        elif (Horario >= 12 and Horario < 18):

            phrases = [
                'Desculpe',
                'Já passou das 11 horas',
                'Estamos no período da tarde',
                'Então, Boa Tarde !',
            ]

            reps = say(phrases)

            return reps

        elif (Horario >= 18 and Horario != 0):
            phrases = [
                'Desculpe',
                'Mas já passou do Horario  da tarde',
                'Agora já está de noite',
            ]

            reps = say(phrases)

            return reps

        if 'boa tarde' in ask:  # Boa Noite Sara

            if Horario >= 0 and Horario < 12:

                pharses = [
                    'Agora não é de tarde',
                    'Ainda é de manhã',
                    'Bom dia'
                ]

                resp = say(pharses)
                return resp

            elif Horario >= 12 and Horario < 18:
                phrases = [
                    'Olá',
                    'Boa tarde'
                ]

                resp = say(pharses)
                return resp

            elif Horario >= 18 and Horario != 0:

                phrases = [
                    'Agora não é de tarde',
                    'Já anoiteceu',
                    'Então, Boa noite !'
                ]

                resp = say(phrases)
                return resp

        if 'boa noite' in ask:  # Boa Noite Sara

            if Horario >= 0 and Horario < 12:

                phrases = [
                    'Agora não é de noite',
                    'Ainda estamos no período diurno',
                    'é de manhã',
                    'Sendo assim, Bom dia'
                ]

                resp = say(phrases)
                return  resp

            elif Horario >= 12 and Horario < 18:
                phrases = [
                    'Agora não é de noite',
                    'Ainda estamos no período da tarde',
                    'Então tenha ótima tarde'
                ]
                
                
            elif Horario >= 18 and Horario != 0:
                phrases = [
                    'Oie',
                    'Boa noite'
                    ]
                
                resp = say(phrases)
                return resp
                
        elif (['treinar', 'iniciar treinamento', 'comesse a treinar'] in ask):
            pharses =  [
                'Tudo bem !',
                'Iniciando treinamento',
                'Aguarde um pouco por favor'
            ]

            treinar()
                


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
