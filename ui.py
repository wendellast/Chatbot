from tkinter import *

from tkinter import ttk
from main import bot_resp



#CONFIG
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
root = Tk()
root.title('SaraWa')
txt = Text(root)




#FUNCTION >>> 
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def respUi():
    return e.get()


def send() -> str:
    
    
    send = f"Você: {e.get()}"
    pergunta = str(e.get().lower())

    resp = bot_resp(pergunta)   



    txt.insert(END, "\n" + send)
    txt.insert(END, "\n" + f'{resp}')
    e.delete(0, END)



#WIDGET >>> 
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send = Button(root, text="send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)

#FINALLY
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
