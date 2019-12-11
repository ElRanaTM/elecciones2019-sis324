# Archivo donde se importa el archovo EXCEL
# Requiere de la libreria Pandas


from time import time
import pandas as pd
from os.path import expanduser as ospath


def importarArchivo():
    tiempo_inicial = time()
    archivo = pd.read_excel(ospath('~/PycharmProjects/Elecciones2019/resources/actas.xlsx'))
    tiempo_final = time()
    print("tiempo de importación: ", tiempo_final - tiempo_inicial)
    return archivo


def generarActas():
    archivo = importarArchivo()
    actas = archivo[['Número Mesa', 'Inscritos', 'CC', 'FPV', 'MTS', 'UCS', 'MAS - IPSP', '21F', 'PDC', 'MNR',
                     'PAN-BOL', 'Votos Válidos', 'Blancos', 'Nulos', 'Estado', 'País', 'Departamento',
                     'Provincia', 'Localidad']]
    return actas


def generarRecintos():
    archivo = importarArchivo()
    recintos = archivo[['Recinto']]
    return recintos


def generarMunicipios():
    archivo = importarArchivo()
    municipios = archivo[['Municipio']]
    return municipios
