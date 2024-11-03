import numpy as np

def calcular_desviacion_estandar(datos_A):
    if len(datos_A) < 2:
        return 0  # No se puede calcular la desviación estándar con menos de 2 datos
    
    desviacion_A = np.std(datos_A)
    return desviacion_A

num_listas_A = int(input("Ingresa la cantidad de listas para las que deseas calcular desviaciones estándar: "))

resultados_A = []
for i in range(num_listas_A):
    entrada_A = input(f"Ingresa la lista {i+1}, si estás en Excel, utiliza la función 'transponer' y pégala aquí: ")
    lista_de_numeros_A = [float(numero) for numero in entrada_A.split('\t')]
    
    desviacion_resultado = calcular_desviacion_estandar(lista_de_numeros_A)
    resultados_A.append(desviacion_resultado)

# Imprimir los resultados de las desviaciones estándar
for i, resultado in enumerate(resultados_A):
    print(f"La desviación estándar para la lista {i+1} es: {resultado}")

# Imprimir la lista con los resultados de desviaciones estándar
print("Lista de resultados de desviaciones estándar:", resultados_A)