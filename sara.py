
import pyttsx3
import chatterbot
import sys

from static.functions.functions import *
from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from difflib import SequenceMatcher
from ui import root




#Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70
args = sys.argv

argv = [

]
argv.append(args)


print(args)
#Chatterbot
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
# Inicialize o ChatBot

def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(
            None,
            message_text,
            candidate_text
        )
        similarity = round(similarity.ratio(),2)
        
        if similarity < ACCEPTANCE:
            similarity = 0.0
        else:
            #print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)
            pass
    return similarity

def select_response(message, list_response, storage=None):
    response = list_response[0]
    #print("resposta escolhida:", response)

    return response

botChat = ChatBot("Sara",
                    read_only=True,
                    statement_comparison_function=comparate_messages,
                    response_selection_method=select_response,
                    
                    
                    logic_adapters=[
                        
                        {
                           
                            "import_path":"chatterbot.logic.MathematicalEvaluation",
                            "import_path":"chatterbot.logic.BestMatch",
                            "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
                           
                        
                        }

])



#Class IA
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
class IA():
    
    def __init__(self):
        super(IA,self).__init__()

    def Sara(self)  :

        
        if ('-U' in argv[0]):
            print('interface')
            root.mainloop()

        else:
            
            print('no')
            #Config
            self.Input = input
            str(self.Input)

            #Loop
            while True:
                
                #Resposta ALTA PROPIEDADE
                """if (self.Input() == 'oi'):
                    print('Olá')
                else:
                    #resposta Chatterbot
                    response = botChat.get_response(self.Input('Qual sua pergunta? '))
                    print(response.text)
                """
                pass






#Finaly
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

Iniciar = IA()
Iniciar.Sara()


