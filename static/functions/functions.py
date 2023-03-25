import pyttsx3
from rich import print
import platform
import sys
from datetime import datetime
from plyer import notification
# Config >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
args = sys.argv  # Pegar argumentos terminal
argv = [

]
argv.append(args)


# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

plataforma = platform.system()

if 'Windows' in plataforma:
    # Trás a função letícia voz
    sara_voz=pyttsx3.init('sapi5')

    # Função de ajuste de voz da sara
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', voz[4].id)
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)

else:
    # Trás a função letícia voz # Se não for a voz leticia padrão é Espeak
    sara_voz=pyttsx3.init()

    # Função de ajuste de voz da sara
    sara_voz.setProperty('voice', 'pt+f2')
    # No 'm2'(masculino) pode colocar 'f2'(feminino) e números até 7
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)


# Functions>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

# Fale, Diz a sara para dizer as frases em voz alta>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def fale(audio):
    #notification.notify(title= "Sara", message = audio, app_name="SaraWA", app_icon="../img/sara_img.png", timeout=3, ticker="2", toast=True)
    # notification.notify(title = "SARA",message = audio,timeout = 3)

    #stream.stop_stream()
   
  
    if ('-U' in argv[0]):
        pass
    else:
        print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
        sara_voz.say(audio)
        sara_voz.runAndWait()         

    # stream.start_stream ()

def faleUi(audio):
      #notification.notify(title= "Sara", message = audio, app_name="SaraWA", app_icon="../img/sara_img.png", timeout=3, ticker="2", toast=True)
    # notification.notify(title = "SARA",message = audio,timeout = 3)

    #stream.stop_stream()
   

    #print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
    sara_voz.say(audio)
    sara_voz.runAndWait()   

        
# Say retorna fala em forma de lista para UI>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def say(args:list) -> str:
    if ('-U' in argv[0]):
           pass
    else:
        strings = [

        ]

        for i in args:
            fale(i)
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

#Hour
def time_hour():
	
	hora = datetime.now()
	horas= hora.strftime('%H horas e %M minutos')
	fale(f'Agora são {horas}')