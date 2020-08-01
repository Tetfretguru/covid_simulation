import random
import matplotlib.pyplot as plt
import plottings as graf
import paises
import alta_pais as pais

def main(simulados_a, simulados_b, y_casos):
    # Casos nuevos nuevos simulados
 
    x_dias = list(range(simulados_a, simulados_b + 1)) 
    
    y_casos = y_casos[simulados_a:simulados_b + 1:]
    
    print(f'Días en curso: {x_dias}')
    print('___' * 20)
    print(f'Casos nuevos por día: {y_casos}')
    print('___' * 20)
    
    #coeffs = np.polyfit(x_dias, y_casos, 1)
    #print(f'Coeficientes: {coeffs}')
 
    menu = f""" Opciones para graficar:
        1 - Activos diarios
        2 - Evolucion total
        """
    opcion = input(menu)

    if opcion == '1':
        return graf.grafica_diaria(x_dias, y_casos)
    elif opcion == '2':
        return graf.grafica_total(x_dias, y_casos)  
    else:
        print('Ingrese opción vñalida')


def run():
    y_casos = pais.daily_cases
    dias_simulados = f""" Al momento de ejecución de este script, hay un total de
        {len(y_casos)} días simulados. Tiene las siguientes opciones:
        
        1. Simular el total de días
        2. Simular por segmentos
        """
    option = input(dias_simulados)

    if option == '1':
        simulados_a = 1
        simulados_b = len(y_casos)
        main(simulados_a, simulados_b, y_casos)
    elif option == '2':
        print('Ingrese el rango "desde/hasta" respectivamente: ')
        simulados_a = int(input('Desde día #: '))
        simulados_b = int(input('Hasta día #: '))
        if str(simulados_a) == True or str(simulados_b) == True:
            print('ERROR: Solo puede ingresar valores enteros.')
            run()
        """
        elif simulados_a or simulados_b > len(y_casos):
            print('ERROR: valores mayores a los disponibles.')
            run()
        """
        main(simulados_a, simulados_b, y_casos)


   


if __name__ == "__main__":
    run()

        