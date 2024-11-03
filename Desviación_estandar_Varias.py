import numpy as np

def calcular_desviacion_estandar(datos):
    if len(datos) < 2:
        return 0  # No se puede calcular la desviación estándar con menos de 2 datos
    
    desviacion = np.std(datos)
    return desviacion

num_listas = int(input("Ingresa la cantidad de listas para las que deseas calcular desviaciones estándar: "))

resultados = []
for i in range(num_listas):
    entrada = input(f"Ingresa la lista {i+1}, si estás en Excel, utiliza la función 'transponer' y pégala aquí: ")
    lista_de_numeros = [float(numero) for numero in entrada.split('\t')]
    
    desviacion_resultado = calcular_desviacion_estandar(lista_de_numeros)
    resultados.append(desviacion_resultado)

# Imprimir los resultados de las desviaciones estándar
for i, resultado in enumerate(resultados):
    print(f"La desviación estándar para la lista {i+1} es: {resultado}")
