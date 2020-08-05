import numpy as np
import alta_pais as alta_pais
import math
 
def regresion(x_dias, y_casos):
    #Regresión lineal - transformamos vectores
    x_dias = np.array(x_dias)
    y_casos = np.array(y_casos)
 
    #Con polyfit calculamos polinomio de la fución
    coeffs = np.polyfit(x_dias, y_casos, 3) #Función cúbica
    print(f'Estos son los coeficientes {coeffs}')
    print('______'*20)
 
    #Cada coeficiente del vector
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]
    d = coeffs[3]
 
    #Gráfica de 3 raíces
    est_y =  a*x_dias**3 + b*x_dias**2 + c*x_dias + d
    print(f'Y axis fitting: {est_y}')
    print(' ')
    print('_____'*20)

    #Estimado de Y
    mu = mean(vector = est_y)
    var = varianza(vector = est_y)
    sigma = desviacion_std(vector = est_y)

    #Vector Y
    mu_y = mean(vector = y_casos)
    var_y = varianza(vector = y_casos)
    sigma_y = desviacion_std(vector = y_casos)


    print(f'Estimado de Y -> media: {mu} varianza: {var} sigma {sigma}')
    print(f'Vector de Y -> media: {mu_y} varianza: {var_y} sigma {sigma_y}')
    print('______'*20)
    return est_y

def mean(vector):
    return sum(vector) / len(vector)

def varianza(vector):
    mu = mean(vector)
    acumulador = 0

    for v in vector:
        acumulador += (v - mu)**2
    return acumulador / len(vector)

def desviacion_std(vector):
    return varianza(vector) ** 0.5
