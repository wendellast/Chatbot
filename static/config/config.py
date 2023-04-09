
from static.functions.functions import speak
import sys
from rich.table import Table
from rich import print
sys.path.append('static/functions/funtions')

# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

# Baner
baner = """

____      _      ____       _    
/ ___|    / \    |  _ \     / \   
 \___ \   / _ \   | |_) |   / _ \  
  ___) |  / ___ \  |  _ <   / ___ \ 
  |____/  /_/   \_\ |_| \_\ /_/   \_\ 


        """


def designer_sara():  # Linha para menu

    # Tabela Sara >>
    table = Table(
        title=f"»»»»»»»»»»»»»»»»»»»»»»»»»»»»»> {baner} <««««««««««««««««««««««««««««««", title_justify='center', title_style='bold blue')

    table.add_column('Informação', justify='center', style=' purple')
    table.add_column('Versão', justify='center', style='bold red')
    table.add_column('Suporte', justify='center', style='bold green')

    # Adicionar linhas nas colunas >>
    table.add_row('Sara, assistente virtual pessoal', '--Beta v1.0--   Compatível: Windows >> Sim;   linux >> Sim;   ',
                  'Contado: Telegram >> https://t.me/Lasstll')

    print(table)

    return 0


def primeira_vez():
    try:
        with open('static/config/cache/cache.txt', 'r', encoding='utf-8') as ler:
            leitura = ler.readline()
        print(leitura)
        if leitura.strip() == 1:
            speak('Hi, my name is Sara.')
            speak('I am your new personal assistant.')
            speak('I am ready to serve you.')
            speak('Please tell me what I can do for you.')
            speak('If you need help, you can say or type "help" to see my commands.')
            with open('static/config/cache/cache.txt', 'w', encoding='utf-8') as new:
                new.write('1')

    except Exception as e:
        print(f"Error: {e}")
        speak('Sorry, I am unable to start. Please try again later.')


primeira_vez()
