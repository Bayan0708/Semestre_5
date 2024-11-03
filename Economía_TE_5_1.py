import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de utilidad Cobb-Douglas
def cobb_douglas_utility(x, y, alpha):
    return x**alpha * y**(1 - alpha)

# Creación de una malla de valores para x e y
x = np.linspace(0.1, 10, 100)
y = np.linspace(0.1, 10, 100)

X, Y = np.meshgrid(x, y)

# Parámetro de la función de utilidad Cobb-Douglas
alpha = 0.5

# Calcula los valores de utilidad para cada combinación de x e y
Z = cobb_douglas_utility(X, Y, alpha)

# Grafica las curvas de indiferencia
plt.figure(figsize=(8, 8))
contour = plt.contour(X, Y, Z, levels=10, cmap='viridis')
plt.clabel(contour, inline=True, fontsize=8)
plt.title('Curvas de Indiferencia')
plt.xlabel('Naranjas')
plt.ylabel('Manzanas')
plt.grid(True)
plt.show()
