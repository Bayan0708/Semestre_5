import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
datos = {
    'x': np.array([35.159, 37.868, 29.491]),
    'y': np.array([5.75803E-05, 6.13822E-05, 4.92197E-05]),
    'colors': ['yellow', 'red', 'green']
}

# Define la función de ajuste (puedes cambiarla según el tipo de ajuste que necesites)
def func(x, a, b):
    return a * x + b

# Ajuste de curva
params, covariance = curve_fit(func, datos['x'], datos['y'])

# Parámetros del ajuste
a, b = params

# Puntos para la línea de ajuste
x_line = np.linspace(min(datos['x']), max(datos['x']), 100)
y_line = func(x_line, a, b)

# Graficar puntos y ajuste de curva
fig, ax = plt.subplots()
for i in range(len(datos['x'])):
    ax.scatter(datos['x'][i], datos['y'][i], label=f'Dato {i+1}', color=datos['colors'][i])

ax.plot(x_line, y_line, label=f'Ajuste de curva: $\\lambda$ = {a:.6f}$\\theta$ + {b:.6f}', color='black')

# Configuración de la gráfica
ax.set_title('$\\lambda$ vs $\\theta$')
ax.set_xlabel('$\\theta$')
ax.set_ylabel('$\\lambda$')
ax.legend()
ax.grid(True)

# Mostrar la gráfica
plt.show()
