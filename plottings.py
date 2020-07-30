import matplotlib.pyplot as plt
import random
import stats as st


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
    y_acumulados = st.acumulados(x_dias, y_casos)
    y_casos = st.recuperados(x_dias, y_casos)
    y_rec_acumulados = st.acumulados(x_dias, y_casos)
   
    plt.title('COVID-19 outbreak simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Total cases')

    plt.plot(x_dias, y_acumulados, label='new cases')
    plt.scatter(x_dias, y_rec_acumulados, label='new cases')
    grafica_acumulados = plt.show()
    
    return grafica_acumulados

def grafica_total_muertes(x_dias, y_casos):
    pass