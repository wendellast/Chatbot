import pyttsx3




sara_voz=pyttsx3.init('sapi5')

# Função de ajuste de voz da sara
voz = sara_voz.getProperty('voices')
sara_voz.setProperty('voice', voz[3].id)
rate = sara_voz.getProperty('rate')
sara_voz.setProperty('rate', rate-50)

sara_voz.say('Olá, eu sou o Sara!')
 
sara_voz.runAndWait()
   
