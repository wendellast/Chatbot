
import pyttsx3
import chatterbot
import sys

from static.functions.functions import botIA
from static.functions.functions import *
from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from difflib import SequenceMatcher
from rich import print



# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
ACCEPTANCE = 0.70  # Txa de acerto

args = sys.argv  # Pegar argumentos terminal
argv = [

]
argv.append(args)

# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

print(args)
# Chatterbot
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*



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
        similarity = round(similarity.ratio(), 2)

        if similarity < ACCEPTANCE:
            similarity = 0.0
        else:
            # print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)
            pass
    return similarity


def select_response(message, list_response, storage=None):
    response = list_response[0]
    # print("resposta escolhida:", response)

    return response


botChat = ChatBot("Sara",
                  read_only=True,
                  statement_comparison_function=comparate_messages,
                  response_selection_method=select_response,


                  logic_adapters=[

                      {

                          "import_path": "chatterbot.logic.MathematicalEvaluation",
                          "import_path": "chatterbot.logic.BestMatch",
                          "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,


                      }

                  ])


# Class IA
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

class IA():

    def __init__(self):
        super(IA, self).__init__()

#Funções
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
    def inputIa(self) -> input:  # desenho input
        Input = input(f"{RED}(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ {END}")
        return Input
#MAIN
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
    def Sara(self):

        # Interface Gráfica
        # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
        if ('-U' in argv[0]):
            from ui import root
            root.mainloop()
            print('interface')
        

        # Terminal
        # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
        else:

            

            # Loop
            while True:
                # Config
                self.Input = self.inputIa()
                str(self.Input.lower())

                if ('sair' in self.Input):
                    break

                # Resposta ALTA PROPIEDADE
                # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
                if ('Bom dia' in self.Input):
                    print('Bom dia')


                # Resposta NíVEL MÉDIO
                # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
                else:
                    # Resposta Chatterbot 
                    response = botChat.get_response(self.Input)

                    if response.confidence > 0.0:
                       print(response.text)


                    #Resposta OpenAI
                    else:
                        resp1 = botIA(self.Input)
                        print(resp1)
                        continue

                


# Finally
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
Iniciar = IA()
Iniciar.Sara()
