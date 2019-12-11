# Archivo donde se generan las actas a partir del archivo ya importado

import importlib.util

spec = importlib.util.spec_from_file_location("actasexcel", "../vista/actasexcel.py")
ActasExcel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ActasExcel)

spec1 = importlib.util.spec_from_file_location("acta", "../modelo/acta.py")
Acta = importlib.util.module_from_spec(spec1)
spec.loader.exec_module(Acta)


def instanciarActas():
    act = ActasExcel.generarActas()
    acta = [len(act)]
    for i in range(len(act)):
        acta[i] = Acta(i, act[i, 0], act[i, 1], act[i, 2], act[i, 3], act[i, 4], act[i, 5], act[i, 6], act[i, 7],
                       act[i, 8], act[i, 9], act[i, 10], act[i, 11], act[i, 12], act[i, 13], act[i, 14], act[i, 15],
                       act[i, 16], act[i, 17], act[i, 18])
    return acta
