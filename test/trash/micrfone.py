from concurrent.futures import ThreadPoolExecutor
import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
        audio = r.listen(s)

        with ThreadPoolExecutor() as executor:
            future = executor.submit(r.recognize_google, audio, language='pt-BR')

        try:
            speech = future.result()
            speech = speech.lower()

        except:
            print('Não entendi, fale novamente')
            return 'none'
    print(speech)
    return speech

recognize_speech()
