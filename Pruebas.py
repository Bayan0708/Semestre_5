import matplotlib.pyplot as plt
import numpy as np

# Valores de x
x = [1, 2, 3, 4, 5]

# Tercera lista de valores de y
y3 = [3, 5, 7, 9, 11]

# Incertidumbre en el eje x para todas las listas
incertidumbre_x = [1, 1, 1, 1, 1]

# Incertidumbre en el eje y solo para la tercera lista
incertidumbre_y3 = [1, 1, 1, 1, 1]

# Cambiar los nombres de los ejes
plt.xlabel("Eje X Personalizado")
plt.ylabel("Eje Y Personalizado")

# Graficar la curva con barras de error en forma de "T"
plt.errorbar(x, y3, xerr=incertidumbre_x, yerr=incertidumbre_y3, fmt='-o', label="Datos promedios", color='black', uplims=True, lolims=True)

# Agregar cuadrícula
plt.grid(True)

# Agregar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
