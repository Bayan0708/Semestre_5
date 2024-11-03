import numpy as np
import matplotlib.pyplot as plt

# Función f(x)
def f(x):
    return (np.abs(np.cos(x + (np.sin(x) / 1.51))) / np.abs(np.cos(x - (np.sin(x) / 1.51))))

# Función g(x)
def g(x):
    return (np.abs(np.cos(x + (np.sin(np.sin(x) / 1.51)))) / np.abs(np.cos(x - (np.sin(np.sin(x) / 1.51)))))

# Rango de valores de x de -0.5 a 2.5
x = np.linspace(0, 2, 1000)

# Calcular los valores correspondientes de y
yf = f(x)

# Calcular los valores correspondientes de y
yg = g(x)

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar la función f(x)
ax.plot(x, yf, label='f(x) teórica con n=1.51')

# Graficar la función f(x)
ax.plot(x, yg, label='g(x) teórica con n=1.51')

# Límites en los ejes x e y
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)

# Dibujar las líneas de los ejes x e y
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Etiquetas de los ejes
ax.set_xlabel('i')
ax.set_ylabel('θ(i)')

# Título del gráfico
#ax.set_title('Graficas f(x) y g(x)')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
