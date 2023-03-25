import json

from rich import print
from rich.table import Table
from static.functions.functions import fale
#Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

#Baner
baner = """

____      _      ____       _    
/ ___|    / \    |  _ \     / \   
 \___ \   / _ \   | |_) |   / _ \  
  ___) |  / ___ \  |  _ <   / ___ \ 
  |____/  /_/   \_\ |_| \_\ /_/   \_\ 


        """

def designer_sara(): # Linha para menu
   
    
    #Tabela Sara >> 
    table = Table(title=f"»»»»»»»»»»»»»»»»»»»»»»»»»»»»»> {baner} <««««««««««««««««««««««««««««««", title_justify='center', title_style='bold blue')
    
    table.add_column('Informação', justify='center', style=' purple')
    table.add_column('Versão', justify='center', style='bold red')
    table.add_column('Suporte', justify='center', style='bold green')
    
    #Adicionar linhas nas colunas >> 
    table.add_row('Sara, assistente virtual pessoal', '--Beta v1.0--   Compatível: Windows >> Sim;   linux >> Sim;   ',  'Contado: Telegram >> https://t.me/Lasstll')
    
    print(table)

    return 0

def primeira_vez():
    ler = open('static/config/cache/cache.txt', 'r')
    leitura = json.loads(ler.read())
    if leitura == 0:
        fale('Oie, Meu nome é Sara')
        fale('A parte de agora sou sua nova assistente pessoal')
        fale('Estou pronta para atender o seus comandos')
        fale('Vai ser um prazer trabalhar com você')
        fale('Vamos lá me diga um comando :)')
        fale('Se você não souber basta digitar ou falar')
        fale('"help comandos" para ver os meus comandos')
        dicionario = 1
        f = open('static/config/cache/cache.txt', 'w+')
        f.write(json.dumps(dicionario))

    elif leitura == 1:
        None

