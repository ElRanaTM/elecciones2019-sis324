# Archivo donde se generan los grafico finales
# Requiere de la libreria matplotlib

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

def imprimirResultados(votos):

    partidos = ['CC', 'FPV', 'MTS', 'UCS', 'MAS - IPSP', '21F', 'PDC', 'MNR', 'PAN-BOL']

    normdata = colors.Normalize(min(votos), max(votos))
    colores = ["b", "g", "r", "c", "m", "y", "k", "w", "b"]

    plt.pie(votos, labels=partidos, autopct="%0.1f %%", colors=colores)
    plt.axis("equal")
    plt.show()

