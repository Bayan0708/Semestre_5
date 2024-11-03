import numpy as np
import matplotlib.pyplot as plt

# Función f(x)
def f(x):
    return (np.abs(np.cos(x + (np.sin(x) / 1.51))) / np.abs(np.cos(x - (np.sin(x) / 1.51))))

# Rango de valores de x de -0.5 a 2.5
x = np.linspace(0, 1.5, 1000)

# Calcular los valores correspondientes de y
y = f(x)

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar la función f(x)
ax.plot(x, y, label='f(x) teórica con n=1.51')

# Coordenadas de los 5 puntos
puntos = [(0.995, 0.017), (0.811, 0.145), (0.554, 0.364), (1.137, 0.122), (1.072, 0.105)]

# Graficar los 5 puntos
for punto in puntos:
    ax.scatter(punto[0], punto[1], color='red', marker='o')

# Texto Puntos experiementales
ax.scatter(punto[0], punto[1], color='red', marker='o',label=f'Puntos experiementales')

# Límites en los ejes x e y
ax.set_xlim(0, 1.5)
ax.set_ylim(0, 1.5)

# Dibujar las líneas de los ejes x e y
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Etiquetas de los ejes
ax.set_xlabel('i')
ax.set_ylabel('θ(i)')

# Título del gráfico
ax.set_title('Comparación del gráfico teórico y experimental')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
