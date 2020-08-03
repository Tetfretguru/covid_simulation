import matplotlib.pyplot as plt
import random
import stats as st


def grafica_activos_diarios(x_dias, y_casos):
    """ A modo de prueba, se usa modelo determinista"""   
    y_fiambres = st.muertos(x_dias, y_casos)
    y_recovered = st.recuperados(x_dias,y_casos)
    
    plt.title('COVID-19 outbreak daily simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Daily new cases')

    plt.plot(x_dias, y_casos, label='New cases')
    plt.plot(x_dias, y_recovered, label='Recovered')
    plt.plot(x_dias, y_fiambres, 'r-', label='Deaths')
    
    plt.legend(loc='best')
    grafica_diarios = plt.show()

    return grafica_diarios

def grafica_casos_totales(x_dias, y_casos):
   
    #y_rec_acumulados = st.acumulados(x_dias, y_casos)
    #y_muertos = st.muertos(x_dias, y_casos)
    
    plt.title('COVID-19 outbreak simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Total cases')

    plt.plot(x_dias, y_casos, label='new cases')
    #plt.plot(x_dias, y_rec_acumulados, label='recovered')
    #plt.plot(x_dias, y_muertos, 'r-', label='deaths')
    plt.legend(loc='best')
    grafica_acumulados = plt.show()
    
    
    return grafica_acumulados

