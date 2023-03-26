import json
import os
def carregar_conversa():
    # define o nome do arquivo a ser utilizado
    arquivo = 'static/memory/memory.json'

    # verifica se o arquivo existe
    if not os.path.isfile(arquivo):
        print(f"O arquivo '{arquivo}' não existe")
        return

    # abre o arquivo em modo de leitura
    with open(arquivo, 'r', encoding='utf-8') as f:
        # carrega o conteúdo do arquivo para um objeto Python
        conversa = json.load(f)

    # percorre a lista de mensagens e imprime cada mensagem em ordem
    for mensagem in sorted(conversa['mensagens'], key=lambda x: x['id']):
        print(f"{mensagem['role']}: {mensagem['content']} (ID: {mensagem['id']})")

    # retorna o objeto Python com a conversa
    return conversa

print(carregar_conversa())