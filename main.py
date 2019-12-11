__author__ = 'David Vargas Lastra'

# from tkinter import *

# from src.vista.menu import Menu
from src.vista.imprimir import imprimirResultados
from src.vista.generartreceporciento import generar13, mediagenerada

def main():
    # root = Tk()
    # menu = Menu(root)
    # menu.mainloop()
    archivo = generar13()
    archivo.head(5)
    media = mediagenerada()
    print(media)
    imprimirResultados(media)


if __name__ == "__main__":
    main()

