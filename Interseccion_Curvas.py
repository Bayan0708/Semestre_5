import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Colocar curvas
def f(x):
    return 5 - x

def g(x):
    return 5 * np.exp(-x)

# Encuentra la primera intersección de las dos curvas utilizando fsolve de SciPy
interseccion1 = fsolve(lambda x: f(x) - g(x), x0=2)
x_interseccion1 = interseccion1[0]
y_interseccion1 = f(x_interseccion1)

# Encuentra la segunda intersección de las dos curvas utilizando fsolve de SciPy
interseccion2 = fsolve(lambda x: f(x) - g(x), x0=4)
x_interseccion2 = interseccion2[0]
y_interseccion2 = f(x_interseccion2)

# Crea un rango de valores para el eje x
x = np.linspace(0, 5, 100)

# Evalua los valores de las funciones para ese rango de valores
y1 = f(x)
y2 = g(x)

# Grafica las curvas
plt.plot(x, y1, label='f(x) = 5 - x')
plt.plot(x, y2, label='g(x) = 5e^(-x)')

# Muestra las intersecciones en el gráfico y etiqueta con sus valores
plt.scatter(x_interseccion1, y_interseccion1, color='red', label=f'Intersección 1: ({x_interseccion1:.3f}, {y_interseccion1:.3f})')
plt.scatter(x_interseccion2, y_interseccion2, color='green', label=f'Intersección 2: ({x_interseccion2:.3f}, {y_interseccion2:.3f})')

plt.annotate(f'({x_interseccion1:.3f}, {y_interseccion1:.3f})', (x_interseccion1, y_interseccion1), textcoords="offset points", xytext=(0, 10), ha='center')
plt.annotate(f'({x_interseccion2:.3f}, {y_interseccion2:.3f})', (x_interseccion2, y_interseccion2), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f"La primera intersección de las curvas está en x = {x_interseccion1:.3f} y su valor es y = {y_interseccion1:.3f}")
print(f"La segunda intersección de las curvas está en x = {x_interseccion2:.3f} y su valor es y = {y_interseccion2:.3f}")
