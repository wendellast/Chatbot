import sys
from rich import print
from main import bot_resp


# Config e var
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

args = sys.argv  # Pegar argumentos terminal
argv = [

]
argv.append(args)

# Cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

print(args)




# Class IA
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*

class IA():

    def __init__(self):
        super(IA, self).__init__()

    #Funções
    # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
    def inputIa(self) -> input:  # desenho input
        Input = input(f"{RED}(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ {END}")
        return Input


    #MAIN
    # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
    def Sara(self):
        Ui = False

        # Config
        # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
        if ('-U' in argv[0]):
            from ui import root
            from ui import respUi
            root.mainloop()
            Ui = True
        

        # Terminal
        # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
             
        # Loop
        while True:
            
            
            # Interface Gráfica
            # *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
            if (Ui == True):   
                self.Input = respUi()
                str(self.Input.lower())
                
            self.Input = self.inputIa()
            self.Input = str(self.Input.lower())

            if('sair' in self.Input):
                break
           
            bot_resp(self.Input)


          
               

                


# Finally
# *=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*
Iniciar = IA()
Iniciar.Sara()
