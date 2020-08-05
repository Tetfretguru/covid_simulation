import matplotlib.pyplot as plt
import numpy as np
import alta_pais as pais 
 
import stats as st
 
 
def grafica_activos_diarios(x_dias, y_casos):
 
   
    estimado_y = st.regresion(x_dias, y_casos)

    plt.title('COVID-19 outbreak daily simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Daily new cases')
 
    plt.plot(x_dias, y_casos, label='Active cases')
    plt.plot(x_dias, estimado_y, label='Polyfit')
    plt.legend(loc='best')
    grafica_diarios = plt.show()
 
    return grafica_diarios
 
def grafica_casos_totales(x_dias, y_casos):
   
    estimado_y = st.regresion(x_dias, y_casos)
    
    plt.title('COVID-19 outbreak simulation')
    plt.xlabel('Days simulated')
    plt.ylabel('Total cases')
 
    plt.plot(x_dias, y_casos, label='new cases')
    plt.plot(x_dias, estimado_y, label='Polyfit')
    plt.legend(loc='best')
    grafica_acumulados = plt.show()
    
    
    return grafica_acumulados
 
def grafica_total_muertos(x_dias, y_casos):
    estimado_y = st.regresion(x_dias, y_casos)
    
    plt.title(f'COVID-19 Total cases Uruguay')
    plt.xlabel('Days simulated')
    plt.ylabel('Total deaths')
 
    plt.plot(x_dias, y_casos, label='Deaths')
    plt.plot(x_dias, estimado_y, label='Polyfit')
    plt.legend(loc='best')
    grafica_muertos = plt.show()
 
    return grafica_muertos