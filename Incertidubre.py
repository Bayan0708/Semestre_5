import numpy as np
import sympy as sp

#Incertidumbres 2 variables

#---------------------------------- Funciones (Creo que puedo solo poner una general) ------------------------------------------------------------------
def calcular_desviacion_estandar_A(datos_A):
    if len(datos_A) < 2:
        return 0  # No se puede calcular la desviación estándar con menos de 2 datos
    
    desviacion_A = np.std(datos_A)
    return desviacion_A

def calcular_desviacion_estandar_B(datos_B):
    if len(datos_B) < 2:
        return 0  # No se puede calcular la desviación estándar con menos de 2 datos
    
    desviacion_B = np.std(datos_B)
    return desviacion_B

#---------------------------------- Derivadas Parciales ------------------------------------------------------------------
    # Definir las variables simbólicas
x, y = sp.symbols('x y')

    # Definir la función en términos de las variables simbólicas
funcion_entrada = input("Ingresa la función en términos de x e y: ")
funcion = sp.sympify(funcion_entrada)  # Convertir la entrada en una expresión simbólica

    # Calcular las derivadas parciales
derivada_x = sp.diff(funcion, x)
derivada_y = sp.diff(funcion, y)

    # Imprimir las derivadas parciales
print("Derivada parcial con respecto a x:", derivada_x)
print("Derivada parcial con respecto a y:", derivada_y)

valor_x = float(input("Ingresa el valor de x: "))
valor_y = float(input("Ingresa el valor de y: "))

    # Evaluar las derivadas en los valores proporcionados
valor_derivada_x = derivada_x.subs({x: valor_x, y: valor_y})
valor_derivada_y = derivada_y.subs({x: valor_x, y: valor_y})

#---------------------------------- Desviación estandar A ------------------------------------------------------------------
num_listas_A = int(input("Ingresa la cantidad de listas para las que deseas calcular desviaciones estándar para tu primer variable: "))

resultados_A = []
for i in range(num_listas_A):
    entrada_A = input(f"Ingresa la lista {i+1}, si estás en Excel, utiliza la función 'transponer' y pégala aquí: ")
    lista_de_numeros_A = [float(numero_A) for numero_A in entrada_A.split('\t')]
    
    desviacion_resultado_A = calcular_desviacion_estandar_A(lista_de_numeros_A)
    resultados_A.append(desviacion_resultado_A)

#---------------------------------- Desviación estandar B ------------------------------------------------------------------
num_listas_B = int(input("Ingresa la cantidad de listas para las que deseas calcular desviaciones estándar para tu segunda varibale: "))

resultados_B = []
for i in range(num_listas_B):
    entrada_B = input(f"Ingresa la lista {i+1}, si estás en Excel, utiliza la función 'transponer' y pégala aquí: ")
    lista_de_numeros_B = [float(numero_B) for numero_B in entrada_B.split('\t')]
    
    desviacion_resultado_B = calcular_desviacion_estandar_B(lista_de_numeros_B)
    resultados_B.append(desviacion_resultado_B)

#---------------------------------- Operaciones para calcular la incertidumbre ------------------------------------------------------------------
    # Multiplicar el número a cada valor de la lista
lista_resultante_A = [valor_A * valor_derivada_x for valor_A in resultados_A]
lista_resultante_B = [valor_B * valor_derivada_y for valor_B in resultados_B]

    # Usar zip() para combinar las listas y luego sumar los pares
lista_suma = [a + b for a, b in zip(lista_resultante_A, lista_resultante_B)]

print(lista_suma)
