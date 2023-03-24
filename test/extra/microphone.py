import speech_recognition as sr

# Cria um objeto de reconhecimento de fala
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source, phrase_time_limit=5)  # Limite de 5 segundos para reconhecimento

    # Tentativa de reconhecer o áudio
    try:
        resp = r.recognize_google(audio, language='pt-BR')
        print(resp)
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala")
    except sr.RequestError as e:
        print(f"Não foi possível completar a requisição: {e}")
    