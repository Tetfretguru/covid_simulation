import random
import matplotlib.pyplot as plt
import plottings as graf

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
 
    menu = """ A continuación, ¿quierés desplegar la gráfica de -casos diarios-
        o -casos acumulados-?

        0 - Casos nuevos diarios
        1 - Casos totales acumulados
        2 - Casos muertes acumuladas

        """
    opcion = input(menu)

    if opcion == '0':
        return graf.grafica_diaria(x_dias, y_casos)
    elif opcion == '1':
        return graf.grafica_total(x_dias, y_casos)
    elif opcion == '2':
        return graf.grafica_total_muertes(x_dias, y_casos)    
    else:
        print('Ingrese opción vñalida')




   





if __name__ == "__main__":
    dias_simulados = int(input('Ingrese cantidad de días a a simular: '))
    main(dias_simulados)