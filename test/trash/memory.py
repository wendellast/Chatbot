import json
import os
from datetime import datetime

def salvar_conversa(pergunta, resposta):
    # define o nome do arquivo a ser utilizado
    arquivo = 'conversa.json'

    # verifica se o arquivo já existe
    if os.path.isfile(arquivo):
        # abre o arquivo existente em modo de leitura
        with open(arquivo, 'r', encoding='utf-8') as f:
            # carrega o conteúdo do arquivo para um objeto Python
            conversa = json.load(f)
    else:
        # se o arquivo não existe, cria um novo objeto Python vazio
        conversa = {'mensagens': []}

    # gera um ID baseado na data e hora atual
    id_mensagem = int(datetime.now().strftime('%Y%m%d%H%M%S%f'))

    # adiciona a nova mensagem à lista de mensagens
    conversa['mensagens'].append({
        'id': id_mensagem,
        'role': 'user',
        'content': pergunta
    })
    conversa['mensagens'].append({
        'id-resp': id_mensagem,
        'role': 'bot',
        'content': resposta,
        'in_reply_to': id_mensagem
    })

    # abre o arquivo em modo de escrita e salva o objeto Python como JSON em UTF-8
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(conversa, f, ensure_ascii=False)

    print(f"Conversa salva com sucesso no arquivo '{arquivo}'")

salvar_conversa('HEHE', 'eu em')