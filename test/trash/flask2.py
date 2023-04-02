from flask import Flask, render_template, request
import openai

# Configurando a chave de API da OpenAI
openai.api_key = "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"

# Iniciando a aplicação Flask
app = Flask(__name__)

# Criando a rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Criando a rota para lidar com a solicitação POST
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Obtendo a mensagem do usuário a partir do formulário
    user_message = request.form['user_message']
    
    # Enviando a mensagem para a OpenAI e recebendo a resposta
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Extraindo a resposta da OpenAI
    bot_message = response.choices[0].text
    
    # Retornando a resposta para a página
    return render_template('index.html', bot_message=bot_message)

if __name__ == '__main__':
    app.run(debug=True)
