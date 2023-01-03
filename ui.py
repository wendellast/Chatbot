from tkinter import *
from static.functions.functions import *
root = Tk()

root.title('Chat')
#CONFIG
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
txt = Text(root)



#FUNCTION >>> 
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
def send():
    
    resp = 'oi'
    send = f"Você: {e.get()}"
    ask = str(e.get())
    resp = botIA(ask)
    txt.insert(END, "\n" + send)

    
    txt.insert(END, "\n" + f'{resp}')

    e.delete(0, END)


#WIDGET >>> 
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
txt.grid(row=0, column=0,columnspan=2)
e = Entry(root, width=100)
send = Button(root, text="send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)

#FINALLY
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

