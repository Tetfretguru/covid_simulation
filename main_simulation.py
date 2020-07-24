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

def grafica_total(x_dias, y_casos):
    #plt.plot(x_dias, est_y)
    plt.plot(x_dias, y_casos)
    grafica_entera = plt.show()
    
    return grafica_entera





if __name__ == "__main__":
    dias_simulados = int(input('Ingrese cantidad de días a a simular: '))
    main(dias_simulados)