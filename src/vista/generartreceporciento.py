# Archivo donde se generan los votos faltantes
# Requiere de las librerias Pandas y Random

from random import random
import pandas as pd
from .actasexcel import importarArchivo


def docerandom():
    ra = 0
    r = [12]
    for i in range(12):
        r = random()
        ra += r
    return ra


def importar():
    acta = importarArchivo()
    return acta


def limpiar():
    actas = importar()
    actaslimpias = actas[actas["Estado"] != 100]
    return actaslimpias


def agrupar():
    agrupadas = limpiar()
    agrupadas.groupby(
       ['Municipio', 'Recinto']
    ).agg({
        'CC': ["mean", "median"],
        'FPV': ["mean", "median"],
        'MTS': ["mean", "median"],
        'UCS': ["mean", "median"],
        'MAS - IPSP': ["mean", "median"],
        '21F': ["mean", "median"],
        'PDC': ["mean", "median"],
        'MNR': ["mean", "median"],
        'PAN-BOL': ["mean", "median"],
        'Votos Válidos': ["mean", "median"],
        'Blancos': ["mean", "median"],
        'Nulos': ["mean", "median"],
    })
    return agrupadas


def generar13():
    generado = agrupar()
    generadototal = pd.DataFrame()
    generadototal['ResultadoCC'] = generado.iloc[:, 13] * (docerandom() - 6)

    generadototal['ResultadoFPV'] = generado.iloc[:, 14] * (docerandom() - 6)

    generadototal['ResultadoMTS'] = generado.iloc[:, 15] * (docerandom() - 6)

    generadototal['ResultadoUCS'] = generado.iloc[:, 16] * (docerandom() - 6)

    generadototal['ResultadoMAS'] = generado.iloc[:, 17] * (docerandom() - 6)

    generadototal['Resultado21F'] = generado.iloc[:, 18] * (docerandom() - 6)

    generadototal['ResultadoPDC'] = generado.iloc[:, 19] * (docerandom() - 6)

    generadototal['ResultadoMNR'] = generado.iloc[:, 20] * (docerandom() - 6)

    generadototal['ResultadoPAN'] = generado.iloc[:, 21] * (docerandom() - 6)

    print("Las actas restantes han sido generadas satisfactoriamente")
    return generadototal


def mediagenerada():
    media = [None] * 9
    gen = generar13()
    media[0] = gen['ResultadoCC'].mean()
    media[1] = gen['ResultadoFPV'].mean()
    media[2] = gen['ResultadoMTS'].mean()
    media[3] = gen['ResultadoUCS'].mean()
    media[4] = gen['ResultadoMAS'].mean()
    media[5] = gen['Resultado21F'].mean()
    media[6] = gen['ResultadoPDC'].mean()
    media[7] = gen['ResultadoMNR'].mean()
    media[8] = gen['ResultadoPAN'].mean()
    for i in range(len(media)):
        media[i] = abs(media[i])
    return media