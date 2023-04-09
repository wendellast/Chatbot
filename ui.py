from tkinter import *
from tkinter import ttk
from main import bot_resp
from static.functions.functions import speakUi
# CONFIG
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
root = Tk()
root.title('SaraWa')
root.configure(bg='#e3c3d3')

# FUNCTION >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*


def send() -> str:
    send = f"Você: {e.get()}"
    pergunta = str(e.get().lower())
    resp = bot_resp(pergunta)
    txt.insert(END, "\n" + send)
    txt.insert(END, "\n" + f'Bot: {resp}')
    speakUi(resp)  # Chamada da função fale()
    e.delete(0, END)


# WIDGET >>>
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
txt = Text(root, width=80, height=20, bg='#e6e6fa', font=('Arial', 12))
txt.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

e = Entry(root, width=80, font=('Arial', 12))
e.grid(row=1, column=0, padx=10, pady=10)

send = Button(root, text="Enviar", font=(
    'Arial', 12), bg='#cc99ff', command=send)
send.grid(row=1, column=1, padx=10, pady=10)

# FINALLY
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
root.mainloop()
