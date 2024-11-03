import numpy as np

def calcular_desviacion_estandar(datos):
    if len(datos) < 2:
        return 0  # No se puede calcular la desviación estándar con menos de 2 datos
    
    desviacion = np.std(datos)
    return desviacion

entrada = input("Ingresa tu lista, si estas en excel utiliza la función transponer y pegala acá: ")
lista_de_numeros = [float(numero) for numero in entrada.split('\t')]    #Convierte la lista a numeros y coloca comas para ser leída
desviacion_resultado = calcular_desviacion_estandar(lista_de_numeros)   
print("La desviación estándar es:", desviacion_resultado)
