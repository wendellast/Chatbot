import pyttsx3
from rich import print

# Config >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

sara_voz = pyttsx3.init()

# Função de ajuste de voz da sara
sara_voz.setProperty('voice', 'pt-br')
# No 'm2'(masculino) pode colocar 'f2'(feminino) e números até 7
rate = sara_voz.getProperty('rate')
sara_voz.setProperty('rate', rate-50)


# Functions>>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

def fale(audio):
    # notification.notify(title = "SARA",message = audio,timeout = 3)

    # stream.stop_stream()
    print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
    sara_voz.say(audio)
    sara_voz.runAndWait()
    # stream.start_stream ()
