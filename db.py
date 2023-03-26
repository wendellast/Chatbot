import sqlite3
import uuid
from datetime import datetime


def salvar_conversa(pergunta, resposta):
    # define o nome do arquivo a ser utilizado
    

    # cria uma conexão com o banco de dados
    conn = sqlite3.connect('conversas.db')

    # cria a tabela de mensagens se ela não existe
    conn.execute('''
        CREATE TABLE IF NOT EXISTS mensagens (
            id TEXT PRIMARY KEY,
            role TEXT,
            content TEXT,
            in_reply_to TEXT
        )
    ''')

    # gera um ID único para a mensagem
    id_mensagem = str(uuid.uuid4())

    # insere a mensagem do usuário na tabela
    conn.execute('''
        INSERT INTO mensagens (id, role, content)
        VALUES (?, ?, ?)
    ''', (id_mensagem, 'user', pergunta))

    # insere a mensagem do bot na tabela
    conn.execute('''
        INSERT INTO mensagens (id, role, content, in_reply_to)
        VALUES (?, ?, ?, ?)
    ''', (str(uuid.uuid4()), 'bot', resposta, id_mensagem))

    # salva as mudanças no banco de dados
    conn.commit()

    # fecha a conexão com o banco de dados
    conn.close()

    print(f"Conversa salva com sucesso no banco de dados 'conversas.db'")


pergunta = input('Pergunta >> ')
resposta = input('Resposta >> ')

salvar_conversa(pergunta, resposta)