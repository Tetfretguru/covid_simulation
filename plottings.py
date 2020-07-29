import matplotlib.pyplot as plt

#Global scope
y_recuperados = []

def recuperados(x_dias, y_casos):
    for i in y_casos:
        y = i * 0.10 
        y_recuperados.append(y)
    return y_recuperados

def grafica_diaria(x_dias, y_casos):
    """ A modo de prueba, se usa modelo determinista"""   
    
    recuperados(x_dias,y_casos)
    plt.scatter(x_dias, y_recuperados, label='recovered')
    
    plt.title('COVID-19 outbreak daily simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Daily new cases')

    plt.plot(x_dias, y_casos, label='new cases')
    grafica_diarios = plt.show()

    return grafica_diarios

def grafica_total(x_dias, y_casos):
    
    recuperados(x_dias,y_casos)

    y_acumulados = []
    y_rec_acumulados = []
    
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
    
    print(f'Total positivos: {y_acumulados}')

    #Se suman los recuperados totales. Se usa 'global y_recuperados'
    j = 0
    y_rec_acumulados.append(y_recuperados[j])
    v_2 = y_recuperados[j] + y_recuperados[j+1]

    while j < len(y_recuperados) - 1:
        v_2 = v_2 + (y_recuperados[j] + y_recuperados[j+1])
        y_rec_acumulados.append(v_2)
        j += 1
    
    print(f'Total recuperados: {y_rec_acumulados}')

    #plt.scatter(x_dias, y_rec_acumulados, label='recovered')
    
    plt.title('COVID-19 outbreak simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Total cases')

    plt.plot(x_dias, y_acumulados, label='new cases')
    plt.scatter(x_dias, y_rec_acumulados, label='new cases')
    grafica_acumulados = plt.show()
    
    return grafica_acumulados
