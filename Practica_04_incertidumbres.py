import numpy as np

# Define las listas de valores y sus incertidumbres
columna1 = [25
,24.9
,24.9
,25
,25
,24.9
,25.1
,25
,25
,24.9
]
incertidumbre1 = [0.07, 0.07, 0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07]

columna2 = [4.0, 5.0, 6.0]
incertidumbre2 = [0.2, 0.1, 0.3]

# Suma de ambas columnas y suma de incertidumbres
suma_columnas = [x + y for x, y in zip(columna1, columna2)]
suma_incertidumbres = [np.sqrt(x**2 + y**2) for x, y in zip(incertidumbre1, incertidumbre2)]

# Producto de los valores y nueva incertidumbre
producto_valores = [x * y for x, y in zip(columna1, columna2)]
nueva_incertidumbre = [x * np.sqrt((y/x)**2 + (z/y)**2) for x, y, z in zip(producto_valores, incertidumbre1, incertidumbre2)]

# División de las dos listas y sus incertidumbres
division_valores = [x / y for x, y in zip(producto_valores, suma_columnas)]
incertidumbre_division = [x * np.sqrt((y/x)**2 + (z/y)**2) for x, y, z in zip(division_valores, nueva_incertidumbre, suma_incertidumbres)]

# Imprime los resultados
print("Suma de ambas columnas:", suma_columnas)
print("Suma de incertidumbres:", suma_incertidumbres)
print("Producto de los valores:", producto_valores)
print("Nueva incertidumbre del producto:", nueva_incertidumbre)
print("División de las dos listas:", division_valores)
print("Incertidumbre de la división:", incertidumbre_division)
