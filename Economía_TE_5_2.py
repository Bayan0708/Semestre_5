import matplotlib.pyplot as plt
import numpy as np

# Parámetros
ingreso_fijo = 100
precio_X = 4
precio_Y = 8

# Rango de valores para X
X = np.linspace(0, ingreso_fijo / precio_X, 100)

# Calcula la restricción presupuestaria para diferentes valores de X
Y = (ingreso_fijo - precio_X * X) / precio_Y

# Cestas de mercado
cestas = {'A': (5, 10), 'B': (8, 6), 'C': (12, 4), 'D': (15, 2)}

# Extraer valores de X e Y para cada cesta
X_vals, Y_vals = zip(*cestas.values())

# Graficar la restricción presupuestaria
plt.plot(X, Y, label='Restricción Presupuestaria', color='blue')

# Graficar las cestas de mercado
plt.scatter(X_vals, Y_vals, label='Cestas de Mercado', color='red')

# Etiquetas y título
plt.xlabel('Bien X')
plt.ylabel('Bien Y')
plt.title('Restricción Presupuestaria y Cestas de Mercado del Consumidor')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
