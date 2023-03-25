import speech_recognition as sr
import sys


from concurrent.futures import ThreadPoolExecutor
from rich import print
from main import bot_resp
from static.functions.functions import fale
from static.config.config import *
from static.config.config import primeira_vez

# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

args = sys.argv  # Pegar argumentos terminal
argv = [

]
argv.append(args)

# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'




# Class IA
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
primeira_vez()
designer_sara()
class IA():

    def __init__(self):
        super(IA, self).__init__()
        
    # Funções
    # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
    def inputIa(self) -> input:  # desenho input
        Input = input(f"{RED}(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ {END}")
        return Input
    
    def inputMic(self):


        r = sr.Recognizer()

        with sr.Microphone() as s:
            print('ouvindo...')
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)

            with ThreadPoolExecutor() as executor:
                future = executor.submit(r.recognize_google, audio, language='pt-BR')

            try:
                speech = future.result()
                speech = speech.lower()

            except:
                print('Não entendi, fale novamente')
                return 'none'

        return speech

    # MAIN
    # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

    def Sara(self):
        Ui = False

        # Config
        # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
        if ('-U' in argv[0]):
            from ui import root
            from ui import respUi
            root.mainloop()
            Ui = True

        # Loop
        while True:
            try:
                
                DIGITAR = True
                if '-d' in argv:
                    DIGITAR = True

                # Interface Gráfica
                # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
                if (Ui == True):
                    self.Input = respUi()
                    str(self.Input.lower())

                # Terminal
                # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
                if (DIGITAR == True):
                    self.Input = self.inputIa()
                    self.Input = str(self.Input.lower())
                else:
                    self.Input = self.inputMic()
                    self.Input = str(self.Input.lower())

                command_close = [
                    'sair', 'fecha','exit',
                    'fechar'
                ]
            
              

                

                if (self.Input in command_close):
                    fale('Tudo bem')
                    fale('Até mais')
                    break
                
                bot_resp(self.Input)
            
            except KeyboardInterrupt:
                fale('Você deseja sair ? Sim? ou Não?')
                
                resp_close = input(f"{RED}(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ {END}")

                if (resp_close.lower() in 'sim' or resp_close.lower() in 'Sim'):
                    fale('Tudo bem')
                    fale('Até mais')
                    break
                elif (resp_close.lower() in 'não' or resp_close.lower() in 'n'):
                    fale('Okay, estou a disposição !')
                    continue
                else:
                    fale('Vou entender como um não')
                    fale('Estou escultando !')
                    continue




# Finally
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
Iniciar = IA()
Iniciar.Sara()
