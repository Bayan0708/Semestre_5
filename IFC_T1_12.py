import numpy as np
from scipy.integrate import quad

# Constantes
h = 6.62607004e-34  # J·s (constante de Planck)
k = 1.38064852e-23  # J/K (constante de Boltzmann)
c = 3e8             # m/s (velocidad de la luz)
T = 2900            # K (temperatura del cuerpo negro)
nu_min = 4e14       # Hz (frecuencia mínima)
nu_max = 7e14       # Hz (frecuencia máxima)

# Función de densidad de energía espectral (Ley de Planck)
def spectral_density(nu):
    return (8 * np.pi * nu**2 / c**3) * (h * nu) / (np.exp((h * nu) / (k * T)) - 1)

# Cálculo de E_total (energía total)
E_total, _ = quad(spectral_density, nu_min, nu_max)

# Cálculo de E_visible (energía en el rango visible)
E_visible, _ = quad(spectral_density, 4e14, 7e14)

# Cálculo del porcentaje de energía visible
porcentaje_visible = (E_visible / E_total) * 100

print(f"Porcentaje de energía emitida en forma de luz visible: {porcentaje_visible:.2f}%")
