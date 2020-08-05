import numpy as np
 
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
    media = (max(est_y) - min(est_y))/ len(est_y)
    print(f'Media "y" : {media}' )
    print('______'*20)
    return est_y