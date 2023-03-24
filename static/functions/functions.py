import pyttsx3
from rich import print
from plyer import notification
import platform
# Config >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

plataforma = platform.system()

if 'Windows' in plataforma:
    # Trás a função letícia voz
    sara_voz=pyttsx3.init('sapi5')

    # Função de ajuste de voz da sara
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', voz[3].id)
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
    print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
    sara_voz.say(audio)
    sara_voz.runAndWait()
   
    # stream.start_stream ()



        
# Say retorna fala em forma de lista para UI>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def say(args:list) -> str:
    strings = [

    ]

    for i in args:
        fale(i)
        strings.append(i)
    
    return "\n".join(strings)
    
def show(args):
    strings = [ 

    ]
    
    for i in args:
        strings.append(i)
    
    return '\n'.join(strings)