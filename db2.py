import sqlite3

def carregar_conversas():
    # cria uma conexão com o banco de dados
    conn = sqlite3.connect('conversas.db')

    # define a consulta SQL para retornar todas as mensagens
    query = "SELECT * FROM mensagens"

    # executa a consulta SQL e retorna as mensagens
    mensagens = conn.execute(query).fetchall()

    # fecha a conexão com o banco de dados
    conn.close()

    # cria um dicionário para armazenar as mensagens
    conversas = {}

    # percorre todas as mensagens e armazena no dicionário
    for mensagem in mensagens:
        id_mensagem = mensagem[0]
        role = mensagem[1]
        content = mensagem[2]
        in_reply_to = mensagem[3]

        # verifica se a mensagem é do usuário ou do bot
        if role == 'user':
            conversas[id_mensagem] = {
                'pergunta': content,
                'resposta': None
            }
        else:
            conversas[in_reply_to]['resposta'] = content

    return conversas




