import matplotlib.pyplot as plt
import numpy as np

# Parámetros iniciales
precio_original = 10
impuesto_por_unidad = 2
cantidad_original = 50

# Función de demanda original (sin impuesto)
def demanda_original(precio):
    return 60 - precio

# Función de oferta original (sin impuesto)
def oferta_original(precio):
    return 10 + precio

# Rango de precios
precios = np.linspace(0, 20, 100)

# Gráfico de oferta y demanda original
plt.plot(precios, demanda_original(precios), label='Demanda Original', color='blue')
plt.plot(precios, oferta_original(precios), label='Oferta Original', color='red')

# Precio y cantidad de equilibrio original
equilibrio_original_precio = precio_original
equilibrio_original_cantidad = demanda_original(equilibrio_original_precio)

# Líneas para marcar equilibrio original
plt.scatter(equilibrio_original_precio, equilibrio_original_cantidad, color='black')
plt.annotate(f'Equilibrio Original\n({equilibrio_original_precio}, {equilibrio_original_cantidad})',
             xy=(equilibrio_original_precio, equilibrio_original_cantidad), xytext=(equilibrio_original_precio + 1, equilibrio_original_cantidad + 5),
             )

# Aplicar el impuesto
precio_con_impuesto = precios + impuesto_por_unidad

# Nueva oferta con impuesto
def oferta_con_impuesto(precio):
    return oferta_original(precio - impuesto_por_unidad)

# Gráfico de oferta con impuesto
plt.plot(precios, oferta_con_impuesto(precios), label='Oferta con Impuesto', linestyle='dashed', color='red')

# Nuevo equilibrio con impuesto
nuevo_equilibrio_precio = equilibrio_original_precio + impuesto_por_unidad
nuevo_equilibrio_cantidad = demanda_original(nuevo_equilibrio_precio)

# Líneas para marcar nuevo equilibrio con impuesto
plt.scatter(nuevo_equilibrio_precio, nuevo_equilibrio_cantidad, color='black')
plt.annotate(f'Nuevo Equilibrio con Impuesto\n({nuevo_equilibrio_precio}, {nuevo_equilibrio_cantidad})',
             xy=(nuevo_equilibrio_precio, nuevo_equilibrio_cantidad), xytext=(nuevo_equilibrio_precio + 1, nuevo_equilibrio_cantidad - 10),
             )

# Etiquetas y título
plt.xlabel('Precio')
plt.ylabel('Cantidad')
plt.title('Efecto de un Impuesto en Oferta y Demanda')
plt.legend()
plt.grid(True)
plt.show()
