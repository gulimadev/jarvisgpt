from main import Main
from asciimatics.screen import Screen
from app import validador

c = Main()
# Screen.wrapper(c.demo)
if __name__ == "__main__":
    teste = input ("Digite algo: ")

    validador(teste)