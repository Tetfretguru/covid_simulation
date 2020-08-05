import random
import matplotlib.pyplot as plt
import numpy as np
 
import plottings as graf
import paises 
import alta_pais as pais
 
def main(simulados_a, simulados_b, y_casos,sub_choice):
    """
    simulados_a = índice origen
    simulados_b = índice final
    y_casos = casos de y axis para gráficar
    sub_choice = condicionante
 
    """
 
    x_dias = list(range(simulados_a, simulados_b + 1)) 
    
    y_casos = y_casos[simulados_a:simulados_b + 1:]
    
    print(f'Días en curso: {x_dias}')
    print('___' * 20)
    print(f'Casos nuevos por día: {y_casos}')
    print('___' * 20)
    

 
    if sub_choice == 'a':
        return graf.grafica_activos_diarios(x_dias, y_casos)
    elif sub_choice == 'b':
        return graf.grafica_casos_totales(x_dias, y_casos)
    elif sub_choice == 'c':
        return graf.grafica_total_muertos(x_dias, y_casos)  
    else:
        print('Ingrese opción válida')
 
 
def run():
    
    dias_simulados = f""" Al momento de ejecución de este script, hay un total de
        {len(pais.pais.active_cases) - 1}  /{len(pais.pais.total_cases)} / {len(pais.pais.total_deaths)} días simulados. Tiene las siguientes opciones:
        
        1. Simular el total de días 
        2. Simular por segmentos
        """
    option = input(dias_simulados)
    
    
 
    if option == '1':
        sub_menu = """ 
        a. Activos diarios
        b. Casos totales
        c. Total muertes
        """
        option_2 = input(sub_menu)
 
        if option_2 == 'a':
            y_casos = active_cases
            simulados_a = 0
            simulados_b = len(y_casos) - 1
            sub_choice = option_2
            main(simulados_a, simulados_b, y_casos, sub_choice)
        elif option_2 == 'b':
            y_casos = total_cases
            simulados_a = 0
            simulados_b = len(y_casos) - 1
            sub_choice = option_2
            main(simulados_a, simulados_b, y_casos, sub_choice)
        elif option_2 == 'c':
            y_casos = total_deaths
            simulados_a = 0
            simulados_b = len(y_casos) - 1
            sub_choice = option_2
            main(simulados_a, simulados_b, y_casos, sub_choice)
        else:
            print('No existe esa opción.')
            print('**********************' * 20)
            print(' ')
            run()
    elif option == '2':
        sub_menu = """ 
        a. Activos diarios
        b. Casos totales
        c. Total muertes
        """
        option_2 = input(sub_menu)
 
        if option_2 == 'a':
            print('Ingrese el rango "desde/hasta" respectivamente: ')
            simulados_a = int(input('Desde día #: '))
            simulados_b = int(input('Hasta día #: '))
            y_casos = daily_cases
            if str(simulados_a) == True or str(simulados_b) == True:
                print('ERROR: Solo puede ingresar valores enteros.')
                run()
            """
            elif simulados_a or simulados_b > len(y_casos):
                print('ERROR: valores mayores a los disponibles.')
                run()
            """
            sub_choice = option_2
            main(simulados_a, simulados_b, y_casos, sub_choice)
        elif option_2 == 'b':
            print('Ingrese el rango "desde/hasta" respectivamente: ')
            simulados_a = int(input('Desde día #: '))
            simulados_b = int(input('Hasta día #: '))
            y_casos = total_cases
            if str(simulados_a) == True or str(simulados_b) == True:
                print('ERROR: Solo puede ingresar valores enteros.')
                run()
            """
            elif simulados_a or simulados_b > len(y_casos):
                print('ERROR: valores mayores a los disponibles.')
                run()
            """
            sub_choice = option_2
            main(simulados_a, simulados_b, y_casos, sub_choice)
        elif option_2 == 'c':
            print('Ingrese el rango "desde/hasta" respectivamente: ')
            simulados_a = int(input('Desde día #: '))
            simulados_b = int(input('Hasta día #: '))
            y_casos = total_cases
            if str(simulados_a) == True or str(simulados_b) == True:
                print('ERROR: Solo puede ingresar valores enteros.')
                run()
            """
            elif simulados_a or simulados_b > len(y_casos):
                print('ERROR: valores mayores a los disponibles.')
                run()
            """
            sub_choice = option_2
            main(simulados_a, simulados_b, y_casos, sub_choice)
        else:
            print('Opción no disponible')
            print('**********************' * 20)
            print(' ')
            run()
 
 
if __name__ == '__main__':
  run()
  
  while True:
    rep = input('¿Simular nuevamente? (s/n): ')
 
    if rep == 's':
      run()
    else:
      break
