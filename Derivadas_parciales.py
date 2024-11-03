import sympy as sp

# Definir las variables simbólicas
x, y = sp.symbols('x y')

# Definir la función en términos de las variables simbólicas
funcion_entrada = input("Ingresa la función en términos de x e y: ")
funcion = sp.sympify(funcion_entrada)  # Convertir la entrada en una expresión simbólica

# Calcular las derivadas parciales
derivada_x = sp.diff(funcion, x)
derivada_y = sp.diff(funcion, y)

# Imprimir las derivadas parciales
print("Derivada parcial con respecto a x:", derivada_x)
print("Derivada parcial con respecto a y:", derivada_y)

valor_x = float(input("Ingresa el valor de x: "))
valor_y = float(input("Ingresa el valor de y: "))

# Evaluar las derivadas en los valores proporcionados
valor_derivada_x = derivada_x.subs({x: valor_x, y: valor_y})
valor_derivada_y = derivada_y.subs({x: valor_x, y: valor_y})

# Imprimir los resultados
print("Derivada parcial con respecto a x en ({}, {}): {}".format(valor_x, valor_y, valor_derivada_x))
print("Derivada parcial con respecto a y en ({}, {}): {}".format(valor_x, valor_y, valor_derivada_y))
