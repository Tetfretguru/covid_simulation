import random


def muertos(x_dias, y_casos):
    y_deaths = []
    
    for i in y_casos:
        y = i / (100 / 38.9) #Porcentaje mundial
        y_deaths.append(y)
    return y_deaths

def recuperados(x_dias, y_casos):
    y_recuperados = []

    for i in y_casos:
        y = i / (100 / 62.3) # Porcentaje mundial
        y_recuperados.append(y)
    return y_recuperados

def acumulados(x_dias, y_casos):
    y_acumulados = []

    # Se suman todos los casos acumulados positivos
    i = 0
    y_acumulados.append(y_casos[i])
    i = 1

    k = 0 # Será el valor del indice para el slice

    while  i < len(y_casos) and k < len(y_casos): 
        delta_y_acumulados = y_acumulados[k::]
        v = sum(delta_y_acumulados) + y_casos[i]
        y_acumulados.append(v)
        k += 1
        i += 1

    print(f'Total positivos: {y_acumulados}') #Sean totales, rec o deaths
    return y_acumulados 