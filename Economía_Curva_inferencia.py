import matplotlib.pyplot as plt
import numpy as np

# Definir funciones de curvas de indiferencia para diferentes niveles de satisfacción
def curva_indiferencia_1(x):
    return 3 / np.sqrt(x)

def curva_indiferencia_2(x):
    return 6 / np.sqrt(x)

def curva_indiferencia_3(x):
    return 9 / np.sqrt(x)

# Crear datos para el eje x
x_vals = np.linspace(0.1, 5, 1000)

# Calcular los valores correspondientes en el eje y para cada curva de indiferencia
y_vals_1 = curva_indiferencia_1(x_vals)
y_vals_2 = curva_indiferencia_2(x_vals)
y_vals_3 = curva_indiferencia_3(x_vals)

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals_1, label='Nivel de Satisfacción 1')
plt.plot(x_vals, y_vals_2, label='Nivel de Satisfacción 2')
plt.plot(x_vals, y_vals_3, label='Nivel de Satisfacción 3')

# Etiquetas y título
plt.title('Curvas de Indiferencia')
plt.xlabel('Bien X')
plt.ylabel('Bien Y')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
