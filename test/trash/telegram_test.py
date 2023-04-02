
import telepot
from static.functions.bots import mess
import time
import openai
# # Defina as chaves de API e token do bot Telegram
# TELEGRAM_TOKEN = ''
# openai.api_key = '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'



messages = mess()
# Configuração da API do OpenAI


TELEGRAM_TOKEN = '5827465386:AAG2veDl-l2mS_Hjepcgef0Y77jzspjTtxU'
OPENAI_API_KEY = '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'

bot = telepot.Bot(TELEGRAM_TOKEN)
def botIAtele(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        # Recebe a mensagem do usuário e envia para a API do OpenAI
        user_input = msg['text']
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = messages
    )
        ChatGPT_reply = response["choices"][0]["message"]["content"]


        messages.append({"role": "assistant", "content": ChatGPT_reply})
        bot.sendMessage(chat_id, ChatGPT_reply)






# Função para processar as mensagens recebidas

# Cria o objeto bot do Telegram
bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(botIAtele)

# Mantém o programa em execução
print('Bot está em execução. Pressione CTRL + C para encerrar.')
while True:
    try:
        time.sleep(0.5)
    except KeyboardInterrupt:
        break
