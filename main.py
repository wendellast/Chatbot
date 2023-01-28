import datetime

from train_sara import treinar
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


        elif (['treinar', 'iniciar treinamento', 'comesse a treinar'] in ask):
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
