import matplotlib.pyplot as plt


def grafica_diaria(x_dias, y_casos):
    """ A modo de prueba, se usa modelo determinista"""   
    y_recuperados = []
    for i in y_casos:
        y = i * 0.10 
        y_recuperados.append(y)
    plt.scatter(x_dias, y_recuperados, label='recovered')
    
    plt.title('COVID-19 outbreak daily simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Daily new cases')

    plt.plot(x_dias, y_casos, label='new cases')
    grafica_diarios = plt.show()

    return grafica_diarios

def grafica_total(x_dias, y_casos):
    y_acumulados = []

    i = 0
    v = y_casos[i] + y_casos[i+1]
    y_acumulados.append(v)
    
    while  i < len(y_casos) - 1:
        v = v + (y_casos[i] + y_casos[i+1])
        y_acumulados.append(v)
        i += 1 

    #plt.scatter(x_dias, y_casos_totales, label='recovered')
    
    plt.title('COVID-19 outbreak simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Total cases')

    plt.plot(x_dias, y_acumulados, label='new cases')
    grafica_acumulados = plt.show()
    
    return grafica_acumulados
