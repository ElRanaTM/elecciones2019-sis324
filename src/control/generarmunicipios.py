# Archivo donde se generan los municipios a partir de los recintos

import importlib.util
from generarrecintos import instanciarRecintos

spec = importlib.util.spec_from_file_location("actasexcel", "../vista/actasexcel.py")
ActasExcel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ActasExcel)

spec1 = importlib.util.spec_from_file_location("acta", "../modelo/municipio.py")
Municipio = importlib.util.module_from_spec(spec1)
spec.loader.exec_module(Municipio)

def instanciarMunicipios():
    mun = ActasExcel.generarMunicipios()
    munici = [len(mun)]
    res = instanciarRecintos()
    for i in range(len(res) + len(mun)):
        munici[i] = res(i, res[i, 0], res[i, 1], res[i, 2], res[i, 3], res[i, 4], res[i, 5], res[i, 6], res[i, 7],
                       res[i, 8], res[i, 9], res[i, 10], res[i, 11], res[i, 12], res[i, 13], res[i, 14], res[i, 15],
                       res[i, 16], res[i, 17], res[i, 18], res[i, 19], mun[i, 0])
    municipio = munici.groupby(['Municipio']).agg({
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
    return municipio
