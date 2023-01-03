import openai

import os


#Config
openai_key = os.getenv('KeyAPI')


openai.api_key = KeyAPI




#OPENAI
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def botIA(ask):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=ask,
        temperature=0.5,
        max_tokens=1024,
        stop=None,
        n=1
        
    )

    message = response.choices[0].text
    
    return message
