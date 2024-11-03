import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = input("x: ")
x = [float(numero) for numero in x.split('\t')]

# Tres listas para los valores de y
y1 = input("y1: ")
y1 = [float(numero) for numero in y1.split('\t')]

y2 = input("y2: ")
y2 = [float(numero) for numero in y2.split('\t')]

# Tercera lista de valores de y
y3 = input("y3: ")
y3 = [float(numero) for numero in y3.split('\t')]

# Incertidumbre en el eje x para todas las listas
incertidumbre_x = input("incertidumbre_x: ")
incertidumbre_x = [float(numero) for numero in incertidumbre_x.split('\t')]

# Incertidumbre en el eje y solo para la tercera lista
incertidumbre_y3 = input("incertidumbre_y: ")
incertidumbre_y3 = [float(numero) for numero in incertidumbre_y3.split('\t')]

# Cambiar los nombres de los ejes
plt.xlabel("Ángulo (θ±0.005)°")
plt.ylabel("Intensidad (y+δy)μW")

# Graficar las curvas
plt.errorbar(x, y1, xerr=incertidumbre_x, yerr=0, fmt='o', label="Datos mínimos experimentales", color='blue')
plt.errorbar(x, y2, xerr=incertidumbre_x, yerr=0, fmt='o', label="Datos máximos experimentales", color='red')
plt.errorbar(x, y3, xerr=incertidumbre_x, yerr=incertidumbre_y3, fmt='--o', label="Datos promedios", color='black')

# Agregar cuadrícula
plt.grid(True)

# Agregar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
