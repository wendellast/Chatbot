from static.functions.bots import *


def bot_resp(pergunta):
    #Resposta do Sistema
    if ('oi' in pergunta):
        print('Hello')

        return 'Hello'

    else:


        # Resposta Chatterbot 
        response = botChat.get_response(pergunta)

        if response.confidence > 0.0:
            print(response.text)
            return response.text

        #Resposta OpenAI
        else:
            resp1 = botIA(pergunta)
            print(resp1)
            return resp1
            

        
        
    
        
        


