# Archivo donde se generan las los recintos a partir de las actas

import importlib.util
from generaractas import instanciarActas

spec = importlib.util.spec_from_file_location("actasexcel", "../vista/actasexcel.py")
ActasExcel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ActasExcel)

spec1 = importlib.util.spec_from_file_location("acta", "../modelo/recinto.py")
Recinto = importlib.util.module_from_spec(spec1)
spec.loader.exec_module(Recinto)

def instanciarRecintos():
    res = ActasExcel.generarRecintos()
    reci = [len(res)]
    act = instanciarActas()
    for i in range(len(act) + len(res)):
        reci[i] = act(i, act[i, 0], act[i, 1], act[i, 2], act[i, 3], act[i, 4], act[i, 5], act[i, 6], act[i, 7],
                       act[i, 8], act[i, 9], act[i, 10], act[i, 11], act[i, 12], act[i, 13], act[i, 14], act[i, 15],
                       act[i, 16], act[i, 17], act[i, 18], res[i, 0])
    recinto = reci.groupby(['Recinto']).agg({
        'CC': "mean",
        'FPV': "mean",
        'MTS': "mean",
        'UCS': "mean",
        'MAS - IPSP': "mean",
        '21F': "mean",
        'PDC': "mean",
        'MNR': "mean",
        'PAN-BOL': "mean",
        'Votos Válidos': "mean",
        'Blancos': "mean",
        'Nulos': "mean",
    })
    return recinto
