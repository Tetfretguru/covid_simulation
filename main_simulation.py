import random
import matplotlib.pyplot as plt

def main(dias_simulados):
    # Casos nuevos nuevos simulados
 
    x_dias = list(range(1, dias_simulados + 1)) 
    
    y_casos = list(random.randint(0, 32) for i in range(dias_simulados))
    
    print(f'Días en curso: {x_dias}')
    print('___' * 20)
    print(f'Casos nuevos por día: {y_casos}')
    print('___' * 20)
    
    #coeffs = np.polyfit(x_dias, y_casos, 1)
    #print(f'Coeficientes: {coeffs}')
 
    return grafica_total(x_dias, y_casos)

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

    plt.plot(x_dias, y_casos_totales, label='new cases')
    grafica_acumulados = plt.show()
    
    return grafica_acumulados



   





if __name__ == "__main__":
    dias_simulados = int(input('Ingrese cantidad de días a a simular: '))
    main(dias_simulados)