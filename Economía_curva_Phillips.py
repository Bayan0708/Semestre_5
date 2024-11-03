import numpy as np
import matplotlib.pyplot as plt

# Función que define la curva de Phillips en forma logarítmica
def philips_curve(unemployment_rate, a, b, inflation_expectations=2.5):
    return np.log(inflation_expectations) - a * np.log(unemployment_rate - 4) + b

# Datos de ejemplo
unemployment_rate = np.linspace(3, 8, 1000)
a = 0.5  # Puedes ajustar este valor
b = 1.5  # Puedes ajustar este valor

# Calcula la inflación usando la curva de Phillips
inflation = philips_curve(unemployment_rate, a, b)

# Grafica la curva de Phillips
plt.figure(figsize=(8, 6))
plt.plot(unemployment_rate, inflation, label='Curva de Phillips', color='blue')
plt.title('Curva de Phillips')
plt.xlabel('Tasa de Desempleo (%)')
plt.ylabel('Inflación')
plt.axvline(4, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
