import matplotlib.pyplot as plt
import numpy as np

# Define la función f(x)
def f(x):
    return (x * 115.1145) / (x - 115.1145)

# Crea un rango de valores de x
x = np.linspace(-115, 300, 400)  # Puedes ajustar el rango según tus necesidades

# Calcula los valores correspondientes de y
y = f(x)

# Define los puntos y sus barras de error
puntos_x = [230.41, 242, 257, 220, 199]  # Aquí puedes definir los valores de x de tus puntos
puntos_y = [230.41, 220, 208.71, 240.53, 272.36] 
barras_de_error = [0.323, 0.323, 0.323, 0.323, 0.323]  # Aquí puedes definir las barras de error correspondientes

# Grafica la función
plt.plot(x, y, label='f(x) = (x * 230.229) / (x - 230.229)')

# Grafica los puntos con barras de error
plt.errorbar(puntos_x, puntos_y, yerr=barras_de_error, fmt='o', label='Puntos con error')

# Configura el gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de f(x) y Puntos con Error')
plt.legend()

# Muestra el gráfico
plt.grid()
plt.show()