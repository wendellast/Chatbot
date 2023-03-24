import datetime
import os

from train_sara import treinar
from rich import print
from static.functions.bots import *
from static.functions.functions import *


# Main >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def bot_resp(ask):
    ask = ask.lower()
    Horario = int(datetime.datetime.now().hour)

    # History
    file_path = 'static/config/temp.txt'
    # olhar se arquivo temp existe
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    try:
        with open(file_path, 'r') as arg:
            if ask in arg.read().splitlines():
                pass
            else:
                with open(file_path, 'a') as arq:
                    arq.write(f'{ask}\n')
    except:
        say(['Desculpe, não foi possível, salvar o seu comando algo deu errado'])

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

            phrases = [
                'Agora não é de tarde',
                'Ainda é de manhã',
                'Bom dia'
            ]

            resp = say(phrases)
            return resp

        elif Horario >= 12 and Horario < 18:
            phrases = [
                'Olá',
                'Boa tarde'
            ]

            resp = say(phrases)
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
            return resp

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

    elif (['treinar', 'iniciar treinamento', 'comesse a treinar'][0] in ask):
        phrases = [
            'Tudo bem !',
            'Iniciando treinamento',
            'Aguarde um pouco por favor'
        ]

        treinar()

    elif (['mostre o histórico', 'abra o histórico', 'historico'][0] in ask):

        try:
            say(['Tudo bem !', ' Eu vou mostra o histórico'])
            phrases = [

            ]

            with open(file_path, 'r') as arg:
                history = arg.read().splitlines()

            for l in history:
                phrases.append(l)

            print(phrases)

            return phrases

        except:
            say(['Desculpe não foi possível mostra o histórico algo deu errado !'])

    elif (['limpar histórico', 'limpar historico', 'apagar histórico', 'delete o histórico', 'apague comandos', 'clear historico'][0] in ask):
        
        say(['Tudo bem,' ' Vou limpar o histórico de comandos !'])
        try:
            with open(file_path, 'r+') as arg:
                arg.truncate(0)
            say(['Histórico limpo com sucesso!'])
        except:
            
            say(['Desculpe, eu não consegue apagar o histórico algo deu errado'])

    else:
        try:

            resp1 = botIA(ask)
            #print(resp1)
            text = str(resp1)
            fale(text)
            
            
            return resp1
        except  Exception as e:
            print(e)    

    #LAgacy
    # # Resposta Chatterbot
        # response = botChat.get_response(ask)
        # if response.confidence > 0.0:
            
        #     print(response.text)
        #     return response.text

        # # Resposta OpenAI
