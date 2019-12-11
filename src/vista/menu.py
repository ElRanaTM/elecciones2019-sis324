# Acá va el menu

from tkinter import *

from .generartreceporciento import *
from .imprimir import *


class Menu:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.leerActasBoton = Button(self.frame, text="Cargar Actas", command=self.leerActas)
        self.leerActasBoton.pack(side=LEFT)

        self.generar13Boton = Button(self.frame, text="Generar 13%", command=generar13)
        self.generar13Boton.pack(side=LEFT)

        self.imprimirBoton = Button(self.frame, text="Imprimir resultados", command=imprimirResultados(mediagenerada()))
        self.imprimirBoton.pack(side=LEFT)

        self.salirBoton = Button(self.frame, text="Salir", command=self.frame.quit)
        self.salirBoton.pack(side=LEFT)

    def leerActas(self, archivo):
        archivo = importar()
        return archivo

    def generar13(self):
        generado = mediagenerada()
        return generado

    def imprimir(self, datos):
        imprimirResultados(datos)
        return

