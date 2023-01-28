import speech_recognition as sr

# Lista os nomes dos microfones disponíveis
print(sr.Microphone.list_microphone_names())

# Cria um objeto de reconhecimento de fala
r = sr.Recognizer()

while True:
    # Ajusta o reconhecimento de fala para o ruído ambiente
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        print("Diga algo...")
        audio = r.listen(source)

    # Tentativa de reconhecer o áudio
    resp = r.recognize_google(audio, language='pt-BR')
    print(resp)
    
