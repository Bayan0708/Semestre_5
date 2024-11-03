import numpy as np
import matplotlib.pyplot as plt

# Función f(x)
def f(x):
    return (4*(np.abs(np.cos(x)*np.sin(x)))+6)

# Rango de valores de x de -0.5 a 2.5
x = np.linspace(0, 2.5, 1000)

# Calcular los valores correspondientes de y
y = f(x)

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar la función f(x)
ax.plot(x, y, label='f(x) teórica con n=1.51')

# Coordenadas minimas
puntosm = [(0, 7.09),
(0.087266463,	7.26	),
(0.174532925	,	7.26),	
(0.261799388	,	7.39),	
(0.34906585	,	7.32)	,
(0.436332313	,	7.32),	
(0.523598776	,	6.94),	
(0.610865238	,	7.06),	
(0.698131701	,	6.86),	
(0.785398163	,	6.12),	
(0.872664626	,	5.76),	
(0.959931089	,	6.11),	
(1.047197551	,	5.97),	
(1.134464014	,	5.51),	
(1.221730476	,	4.84),	
(1.308996939	,	4.85),	
(1.396263402	,	4.86),	
(1.483529864	,	4.92),	
(1.570796327	,	4.79),	
(1.658062789	,	4.63),	
(1.745329252		,4.5)	]

# Coordenadas maximas
puntosM =[
(0	,	7.22),
(0.087266463,	7.32),
(0.174532925	,	7.35),
(0.261799388	,	7.45),
(0.34906585	,	7.45),
(0.436332313	,	7.42),
(0.523598776	,	7.65),
(0.610865238	,	7.19),
(0.698131701	,	6.96),
(0.785398163	,	6.73),
(0.872664626	,	6.47),
(0.959931089	,	6.24),
(1.047197551	,	6.07),
(1.134464014	,	5.65),
(1.221730476	,	5.45),
(1.308996939	,	5.45),
(1.396263402	,	4.96),
(1.483529864	,	5.09),
(1.570796327	,	4.86),
(1.658062789	,	4.76),
(1.745329252	,	4.59 )   
]

# Graficar minimos
for puntom in puntosm:
    ax.scatter(puntom[0], puntom[1], color='red', marker='o')

# Graficar maximos
for puntoM in puntosM:
    ax.scatter(puntoM[0], puntoM[1], color='black', marker='o')

# Texto Puntos experiementales
ax.scatter(puntom[0], puntom[1], color='red', marker='o', label='Puntos experimentales')

# Límites en los ejes x e y
ax.set_xlim(0, 3)
ax.set_ylim(0, 8)

# Dibujar las líneas de los ejes x e y
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Etiquetas de los ejes
ax.set_xlabel('i (grados)')
ax.set_ylabel('θ(i)')

# Título del gráfico
ax.set_title('Comparación del gráfico teórico y experimental')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()


